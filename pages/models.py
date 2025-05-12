from django.db import models
from autoslug import AutoSlugField

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True, null=True)
    template = models.ForeignKey('themes.PageTemplate', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # SEO Fields
    meta_title = models.CharField(max_length=60, help_text="SEO title (max 60 chars)", blank=True)
    meta_description = models.CharField(max_length=160, help_text="SEO description (max 160 chars)", blank=True)
    og_title = models.CharField(max_length=60, blank=True)
    og_description = models.CharField(max_length=160, blank=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True, null=True)

    # Pricing Fields
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pricing_benefits = models.TextField(default="""Functional Website Template
        Responsive Web Design
        Fully Working Contact Form
        Django Admin Panel
        Easy Customization – Under 20 Minutes""")
    pricing_bonuses = models.TextField(blank=True, help_text="Bonus items (line break separated)")

    def get_canonical_url(self):
        return f"https://{self.domain.name}/"

    def __str__(self):
        return self.title

class Section(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero'),
        ('benefits', 'Benefits/Value Proposition'),
        ('how_it_works', 'How It Works'),
        ('pricing', 'Pricing'),
        ('faq', 'FAQ'),
        ('final_cta', 'Final CTA')
    ]
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    order = models.PositiveIntegerField()
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    image = models.ImageField(upload_to='section_images/', null=True, blank=True)
    icon = models.CharField(max_length=100, help_text="Font Awesome or Feather icon class", blank=True)
    heading = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sections/', blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.page.title} - {self.section_type}"

class FAQ(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='faqs'
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question