
---

### `views.md` – Core Logic

```markdown
# Views & Webhooks

All logic lives in `core/views.py`.

---

## 🛠 Key Views

### `landing_page(request)`
Detects domain → renders correct landing page

```python
def landing_page(request):
    raw_host = request.get_host()
    host = raw_host.split(':')[0].lower().strip()

    try:
        domain = Domain.objects.select_related('page').get(name__iexact=host)
        page = domain.page
    except Domain.DoesNotExist:
        return HttpResponse("Domain not live yet.", status=404)

    return render(request, 'landing_page_neon.html', {'page': page})
```

### Stripe integration
```python
def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': settings.STRIPE_PRICE_ID,
            'quantity': 1
        }],
        mode='payment',
        success_url=settings.BASE_URL + reverse("payment_successful") + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=settings.BASE_URL + reverse("payment_cancelled"),
        client_reference_id=request.get_host(),
    )
    return redirect(session.url, code=303)
```

### Stripe webhook
```python
@require_POST
@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        logger.error("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        logger.error("Signature verification failed")
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        email = session.customer_details.email
        domain = session.client_reference_id

        download_url = generate_presigned_url(email)
        UserPayment.objects.create(email=email, download_url=download_url)

        posthog.capture(domain, 'purchase_completed', {
            'email': email,
            'domain': domain
        })

        return HttpResponse(status=200)
    return HttpResponse(status=204)
```

### Dynamic sitemap
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def sitemap_xml(request):
    domain = request.get_host().split(':')[0].lower()
    return render(request, 'sitemap.xml', {
        'domain': domain,
        'today': timezone.now()
    }, content_type='application/xml')
```

### Dynamic robots.txt
```python
def robots_txt(request):
    domain = request.get_host().split(':')[0].lower()
    return render(request, 'robots.txt', {
        'domain': domain
    }, content_type='text/plain')
```

