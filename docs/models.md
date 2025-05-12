# Django Models Overview

The core of the landing page engine is built around these models:

## 🧾 Page Model

Stores the main landing page data.

```python
class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    # SEO Fields
    meta_title = models.CharField(max_length=60, help_text="SEO title (max 60 chars)", blank=True)
    meta_description = models.CharField(max_length=160, help_text="SEO description", blank=True)

    # Pricing
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pricing_benefits = models.TextField(blank=True, default="Functional Website Template\nResponsive Design\nContact Form\nDjango Admin Panel\nEasy Setup")

```
## Domain Model
Maps domains to pages.

```python
class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='domains')
```

## Section Model
Renders dynamic copy per landing page

```python
class Section(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero'),
        ('benefits', 'Benefits'),
        ('pricing', 'Pricing'),
        ('faq', 'FAQ'),
        ('final_cta', 'Final CTA')
    ]

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    order = models.PositiveIntegerField()
    heading = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.URLField(blank=True)
```

## FAQ model
Reusable questions across all landing pages
```python
class FAQ(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
```