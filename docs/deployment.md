
---

### `deployment.md` – Deploying to Linode

```markdown
# Deployment Guide

How to deploy the Django landing page engine to production (Linode or any Linux server).

---

## 🚀 Prerequisites

- ✅ Django app working locally
- ✅ 40 domains ready
- ✅ Nginx configured to accept all domains
- ✅ Gunicorn + Uvicorn (or Daphne) running
- ✅ Static/media files collected
- ✅ Stripe & Posthog keys added

---

## 🧱 Steps to Deploy

1. Download code
2. Install dependencies, make migrations, run initial setup with my install.sh:
```bash
chmod +x install.sh
./install.sh
```
3. Set up VPS following this guide: https://github.com/cangeorgecode/django_vps_setup
4. In the /etc/nginx/sites-available/app_name (Nginx file):
```
server {
    listen 80;
    server_name <domain_name>;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/django_app/<app1_name>.sock;
    }
}
```
In the "domain_name", add all the domain names you are routing to the app

5. When you run certbot to obtain SSL, you must do it for all domains in one go. If you do one domain at a time, it won't work. 