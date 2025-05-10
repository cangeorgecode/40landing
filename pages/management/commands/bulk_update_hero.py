from django.core.management.base import BaseCommand
from pages.models import Page, Section
import random

class Command(BaseCommand):
    help = "Update hero sections of all landing pages with keyword-rich copy"

    def handle(self, *args, **kwargs):
        # Keyword-rich headline options
        headlines = [
            "Premium Business Website Template",
            "Functional Django Website – Ready to Go",
            "Best HTML Template for Small Businesses",
            "Fully Built Django Business Site",
            "Modern Website Design – Out of the Box",
            "Professional Website Template – No Coding",
            "Responsive Business Website Template",
            "Django-Powered Business Website",
            "Easy-to-Customize Web Template",
            "Launch Your Business Online Fast"
        ]

        # Subheadlines
        subheadlines = [
            "A fully functional business website template built with Django. Setup in 20 minutes.",
            "Includes contact form, admin panel, and premium design – ready to deploy.",
            "No developer experience needed – just clone, customize, and go live.",
            "Perfect for small businesses, startups, and founders who want a clean site fast.",
            "Django backend + admin included – easy content management from day one.",
            "Built with Tailwind CSS & DaisyUI – modern, responsive, and fast to load.",
            "Complete with working contact form and professional layout.",
            "Ready to deploy on any platform – Linode, Render, Heroku, Vercel",
            "Start with a beautiful, functional template – no coding required.",
            "Clean codebase. Simple setup. Professional results."
        ]

        # CTA Buttons
        cta_buttons = [
            ("Download Now – Setup in 20 Minutes", "/checkout/"),
            ("Buy Now – Launch Today", "/checkout/"),
            ("Get the Template – No Dev Skills Needed", "/checkout/"),
            ("Instant Access – Clone & Go Live", "/checkout/"),
            ("Start Fast – Business Website Template", "/checkout/"),
            ("Skip the Setup – Download Now", "/checkout/")
        ]

        # Update all pages
        pages = Page.objects.all()

        for i, page in enumerate(pages):
            try:
                hero_section = page.sections.get(section_type='hero')
            except Section.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"No hero section for {page.title}"))
                continue

            # Assign new content
            hero_section.heading = random.choice(headlines)
            hero_section.content = random.choice(subheadlines)
            hero_section.button_text, hero_section.button_link = random.choice(cta_buttons)

            hero_section.save()
            self.stdout.write(self.style.SUCCESS(f"Updated hero for {page.title}"))

        self.stdout.write(self.style.SUCCESS("✅ All hero sections updated with fresh copy"))