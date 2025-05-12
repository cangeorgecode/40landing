
---

### `stripe.md` – Payment Flow

```markdown
# Stripe Integration

Stripe handles all purchases across 40 domains using one webhook and price ID.

---

## 🧱 Key Files

- `settings.py` – API keys, price ID
- `views.py` – Checkout + Webhook logic
- `UserPayment` – Tracks who paid
- `DOMAIN_MODEL` – Maps domains to pages

---

## 🛠 Setup Instructions

### 1. Get Stripe Keys

Add to `.env` or shell:

```bash
export STRIPE_SECRET_KEY=sk_test_XXXXXXXXXXXXXX
export STRIPE_WEBHOOK_SECRET=whsec_XXXXXXXXXXXXX
export STRIPE_PRICE_ID=price_XXXXXXXXXXXXXX
```

### 2. Get Webhook secrets from "Developer" tab in Stripe (for production)

### 2.1 For testings, run stripe in cli to test webhook:
```
stripe listen --forward-to http://localhost:8000/stripe/webhook/
```
Don't forget the trailing /

Replace "/stripe/webhook/" with your webhook path

### 3 Webhook flow
1. Visitor lands on yourmaindomain.com  
2. Clicks “Buy Now”  
3. Redirected to Stripe Checkout
4. Stripe sends webhook to yourmaindomain.com/webhook/stripe/
5. Webhook finds origin domain via client_reference_id
6. Generates pre-signed S3 link
7. Sends to Posthog for tracking
8. Redirects user to /download/?url=PRE_SIGNED_S3_URL