
---

### `posthog.md` – Conversion Tracking

```markdown
# Posthog Tracking

Used to track which domains convert best.

---

## 🧰 Events Tracked

| Event | When It Fires |
|-------|---------------|
| `page_view` | On landing page load |
| `cta_clicked` | When someone clicks “Buy Now” |
| `purchase_completed` | After successful payment |

---

## 📈 How to Analyze in Posthog

Go to [Posthog Insights](https://app.posthog.com/insight/trend )

Click **“Break down by property”** → choose `landing_domain`

Build funnels like:

1. `page_view_with_domain`
2. `cta_clicked`
3. `purchase_completed`

Filter by:
- Domain
- Date
- Email (if available)

---

## 📦 Optional: Export Data

Use Posthog API or CSV export to get:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://app.posthog.com/api/projects/your_project_id/insights/trend/ " \
     --get \
     --data-urlencode "events=[{'id':'page_view','type':'events','order':0}]" \
     --data-urlencode "breakdown=landing_domain" \
     --data-urlencode "date_from=-30d"
```

Save results → build dashboards → optimize conversions.