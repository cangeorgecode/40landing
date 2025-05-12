
---

### `templates.md` – How Templates Work

```markdown
# Templates

All landing pages extend `base.html`  
Each domain uses the same set of templates but shows different content via `Section` model.

---

## 🧱 Base Template (`base.html`)

```HTML
{% load static tailwind_tags %}
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    {% tailwind_css %}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/daisyui @latest/dist/full.min.css" />
    <script defer src="{% static 'htmx.min.js' %}"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.7/gsap.min.js "></script>

    <!-- Posthog -->
    <script src="//app.posthog.com/js/ph.js" async></script>
    <script>
        posthog.init("your_posthog_api_key", {
          api_host: "https://app.posthog.com ",
          person_profiles: 'always'
        });
    </script>

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter :wght@400;600;700&family=Fira+Code&display=swap" rel="stylesheet">

    <!-- Custom Styles -->
    <style>
        .glow { box-shadow: 0 0 15px rgba(255, 107, 0, 0.4); }
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-base-100 via-neutral-50 to-base-100 text-base-content flex flex-col">
    {% include "partials/navbar.html" %}
    {% block content %}{% endblock %}
    {% include "partials/footer.html" %}
</body>
</html>
```

### Landing page template (landing_page_neon.html)

```HTML
{% extends "base.html" %}
{% load custom_filters %}

{% block content %}
    {% for section in page.sections.all %}
        {% if section.section_type == 'hero' %}
            <!-- Hero Section -->
        {% elif section.section_type == 'benefits' %}
            <!-- Benefits Section -->
        {% elif section.section_type == 'how_it_works' %}
            <!-- How It Works Section -->
        {% elif section.section_type == 'pricing' %}
            <!-- Pricing Section -->
        {% elif section.section_type == 'faq' %}
            <!-- FAQ Section -->
        {% elif section.section_type == 'final_cta' %}
            <!-- Final CTA -->
        {% endif %}
    {% endfor %}
{% endblock %}
```

