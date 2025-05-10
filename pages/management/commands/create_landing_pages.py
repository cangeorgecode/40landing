# pages/management/commands/create_landing_pages.py

from django.core.management.base import BaseCommand
from pages.models import Page, Section
from core.models import Domain
from themes.models import PageTemplate  # Make sure this is correct
import random

class Command(BaseCommand):
    help = 'Creates 40 landing pages with matching domains and sections'

    def handle(self, *args, **kwargs):
        # Get template from DB
        try:
            default_template = PageTemplate.objects.get(name='Neon Pulse')  # Or whatever name you gave in admin
        except PageTemplate.DoesNotExist:
            self.stdout.write(self.style.ERROR("No PageTemplate found. Please create one first."))

        # Sample content for variation
        titles = [
            "Django SaaS Kit", "Rapid Django Setup", "SaaS Boilerplate",
            "Django Launchpad", "Full-Stack Django", "Django Starter Kit",
            "Build Faster with Django", "Django Launchkit", "Build professional website fast",
            "Set up professional website in 20 mins"
        ]

        hero_headings = [
            "Launch Your SaaS in Hours",
            "Start Fast with Django",
            "Skip the Boring Stuff – Build Faster",
            "Your SaaS Starter Kit",
            "The Ultimate Django Template",
            "No More Setup Time – Just Code",
            "From Zero to Deploy in Minutes",
            "Pre-Built Django Admin Dashboard",
            "Stripe Ready – Start Selling Today",
            "Tailwind + DaisyUI + HTMX Included",
        ]

        hero_contents = [
            "Pre-built Django boilerplate with authentication, Stripe integration, admin dashboard, and more.",
            "Save 10+ hours of setup time and start building your product.",
            "One-time purchase. No subscription. Lifetime access.",
            "Perfect for indie hackers, founders, and developers.",
            "Includes email capture, analytics, and support.",
            "Ready to deploy on Vercel, Render, or Linode.",
            "Built with Tailwind CSS, DaisyUI, and Alpine.js.",
            "Fast setup – clone, install, launch.",
            "Get paid faster – built-in Stripe Checkout.",
            "All future updates included at no extra cost."
        ]

        cta_buttons = [
            "Get Started Now", "Download Now", "Buy & Launch Today",
            "Start Building", "Skip Setup", "Start making money today",
            "Instant Download", "Launch Faster", "Start in Minutes",
            "Save 10+ Hours"
        ]

        # Create 40 pages
        for i in range(3, 41):
            page_title = f"{random.choice(titles)} #{i}"
            slug = f"landing-{i}"

            page = Page.objects.create(
                title=page_title,
                slug=slug,
                description="Pre-built Django starter kit with Stripe, Tailwind, and more.",
                template=default_template,
                meta_title=f"{page_title} | Save 10+ Hours",
                meta_description="Django SaaS kit that saves dev time and helps you launch fast.",
                original_price=1394,
                current_price=697,
                pricing_benefits="Full Django SaaS Boilerplate\nStripe integration ready to go\nAdmin dashboard + analytics\nEmail capture + newsletter system",
                pricing_bonuses="Free IT support for 30 days\nAuto-setup bash script",
            )

            # Add Sections
            Section.objects.create(
                page=page,
                order=1,
                section_type='hero',
                heading=random.choice(hero_headings),
                content=random.choice(hero_contents),
                button_text=random.choice(cta_buttons),
                button_link="/checkout/"
            )

            Section.objects.create(
                page=page,
                order=2,
                section_type='benefits',
                heading="This Is Not Just Code — It's Your Headstart",
                content=f"If you're trying to launch fast, setup time = lost income. That's why we built this kit.\n\nfas fa-stopwatch\nSave Time\nNo more copying boilerplate manually\n\nfas fa-dollar-sign\nStart Getting Paid\nStripe integration included – start accepting payments immediately\n\nfas fa-laptop-code\nFocus on Building\nSkip boring setup – jump straight into building what matters",
            )

            Section.objects.create(
                page=page,
                order=3,
                section_type='final_cta',
                heading="Still Have Questions?",
                content="No risk. 30-day money-back guarantee.",
                button_text="Buy NOW – Save 10+ Hours",
                button_link="/checkout/",
            )

            # Create domain entry
            domain_name = f"landing{i}.com"
            Domain.objects.create(
                name=domain_name,
                page=page
            )

            self.stdout.write(self.style.SUCCESS(f"✅ Created: {page.title} → {domain_name}"))

        self.stdout.write(self.style.SUCCESS("🎉 All 40 landing pages created!"))