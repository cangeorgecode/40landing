# Django + HTMX SaaS Boilerplate Pro 🚀
Thank you for purchasing the Pro SaaS Boilerplate  


&nbsp;


## Contact Me 📧  
- Email: george@superuserweb.dev  
- X: @joji_jiji    
- Discord: Coming soon

I will try to respond with 24 hours. 🙏


&nbsp;


## Setup 🔧

```
# Unzip the file

# Go to where the files are located
cd <dir_name>

# Activate virtual environment and install python packages
source venv/bin/activate
pip install -r requirements.txt

# Install Tailwind using the Django-Tailwind package
python manage.py tailwind install
cd theme/static_src
npm i daisyui@latest
cd ../..
python manage.py tailwind build
python manage.py collecstatic --noinput

# Migrate database
python manage.py migrate

# Check that everything is running
python manage.py runserver

```


&nbsp;


## ⚠️ Before you deploy your app ⚠️

Do not forget to set debug=False in settings.py


&nbsp;


## Configuring .env file 🔒

You will need:

#### Email host and password (for django-allauth)  
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD

#### Stripe secret keys 
- STRIPE_PUBLISHABLE_KEY = 'YOUR_KEY_HERE'  
- STRIPE_SECRET_KEY = 'YOUR_KEY_HERE'  
- STRIPE_WEBHOOK_SECRET = 'YOUR_SECRET_HERE'  

#### Product 1  
- PRO_PRODUCT_ID = 'YOUR_PRODUCT_ID_HERE'  
- PRO_PRICE_ID = 'YOUR_PRODUCT_PRICE_ID_HERE'  

#### Product 2  
- ENTERPRISE_PRODUCT_ID = 'YOUR_OTHER_PRODUCT_ID_HERE'  
- ENT_PRICE_ID = 'YOUR_OTHER_PRODUCT_PRICE_ID_HERE'  


&nbsp;


## Built with your favourite tech stack 🤖

- Django
- Tailwind
- DaisyUI  
- HTMX  
- Alpine.js


&nbsp;


## Features exclusive to Pro version (available now) 🧩  

- Stripe (one-off) payment
- User management dashboard
- Email template
- Django Rest Framework
- CSV import/export

&nbsp;


## Features coming soon 🚧  

- Stripe (subscriptions) payment
- Social media login
- Posthog analytics
- Sentry logging
- Multi-tenancy
- Deployment script
- Redis, Celery integration
- Docker setup


&nbsp;


## Security
To enable HTTPS in production, configure your web server (e.g., Nginx) with an SSL certificate (e.g., Let's Encrypt). In development, use `runserver` with caution as it doesn't support HTTPS natively—consider a tool like `django-sslserver` for local testing.


&nbsp;


## How-to guides, marketing and copywriting tips 🗞️  

- Blog (no sign up needed): https://joji.beehiiv.com
