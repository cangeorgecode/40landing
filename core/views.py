from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *
from pages.models import *
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
import logging
import os
import stripe
import boto3
from botocore.exceptions import ClientError
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from .models import UserPayment


# Stripe configs
stripe.api_key = settings.STRIPE_SECRET_KEY

# Configure logging
log_file_path = os.path.join(settings.BASE_DIR, 'logs', 'app.log')  # Path to the log file
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)  # Ensure the directory exists

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# AWS configs
s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)

def landing_page(request):
    raw_host = request.get_host()
    host = raw_host.split(':')[0].lower().strip()

    try:
        domain = Domain.objects.select_related('page').get(name__iexact=host)
        page = domain.page
    except Domain.DoesNotExist:
        return HttpResponse("Domain not live yet.", status=404)

    if request.path in ['/checkout/', '/payment-successful/', '/payment-cancelled/', '/webhook/stripe/']:
        return None  # Let other views handle it

    return render(request, 'landing_page_neon.html', {'page': page})

def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': settings.PRODUCT_PRICE_ID,  # Replace with your Price ID from Stripe
            'quantity': 1,
        }],
        mode='payment',
        success_url = f'{settings.BASE_URL}{reverse("payment_successful")}?session_id={{CHECKOUT_SESSION_ID}}',
        cancel_url = f'{settings.BASE_URL}{reverse("payment_cancelled")}',
        customer_email=None,  # Stripe will prompt for email
    )
    return redirect(session.url, code=303)

def payment_successful(request):
    session_id = request.GET.get('session_id')
    
    if not session_id:
        return HttpResponse("Invalid session ID", status=400)

    session = stripe.checkout.Session.retrieve(session_id)
    customer_email = session.customer_details.email

    try:
        user_payment = UserPayment.objects.get(email=customer_email, has_paid=True)
    except UserPayment.DoesNotExist:
        return render(request, 'core/payment_cancelled.html')

    # Store URL in session instead of query string
    request.session['download_url'] = user_payment.download_url
    return redirect('download_page')

def payment_cancelled(request):
    return render(request, 'core/payment_cancelled.html')

def download_page(request):
    download_url = request.session.pop('download_url', None)
    if not download_url:
        return HttpResponse("Download URL missing. Please contact support.", status=400)

    return render(request, 'core/download.html', {'download_url': download_url})

@require_POST
@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        logger.error("Webhook failed at event construction")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        logger.error("Webhook signature verification failed")
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        email = session['customer_details']['email']

        # Generate S3 URL
        try:
            download_url = s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': settings.AWS_STORAGE_BUCKET, 'Key': settings.AWS_FILE_KEY},
                ExpiresIn=86400  # 24 hours
            )
        except ClientError as e:
            logger.error(f"S3 URL generation failed for {email}: {str(e)}")
            return HttpResponse(status=500)

        # Save or update UserPayment
        user_payment, created = UserPayment.objects.update_or_create(
            email=email,
            defaults={
                'has_paid': True,
                'download_url': download_url
            }
        )

        # Optional: Log successful payment
        logger.info(f"Checkout completed by {email}")

        return HttpResponse(status=200)

    return HttpResponse(status=204)

def terms(request):
    return render(request, 'core/terms.html')

def privacy(request):
    return render(request, 'core/privacy.html')