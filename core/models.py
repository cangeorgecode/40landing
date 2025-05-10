from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField

class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)  # e.g., "kit1.com"
    page = models.ForeignKey('pages.Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserPayment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    has_paid = models.BooleanField(default=False)
    download_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.has_paid}"