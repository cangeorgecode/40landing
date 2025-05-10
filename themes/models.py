from django.db import models

class PageTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    html_content = models.TextField(help_text="Use {{ page.title }}, {{ section.heading }} etc. as placeholders")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name