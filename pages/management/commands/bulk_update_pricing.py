from django.core.management.base import BaseCommand
from pages.models import Page

class Command(BaseCommand):
    help = "Set pricing info for all pages"

    def handle(self, *args, **kwargs):
        pages = Page.objects.all()
        updated_count = 0

        for page in pages:
            page.original_price = 1394
            page.current_price = 697
            page.pricing_benefits = """Functional Website Template
                Responsive Web Design
                Fully Working Contact Form
                Django Admin Panel
                Easy Setup – Under 20 Minutes"""
            page.pricing_bonuses = """Free IT Support for 30 Days
                Auto-Setup Bash Script"""
            page.save()
            updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Updated {updated_count} pages with pricing info"))