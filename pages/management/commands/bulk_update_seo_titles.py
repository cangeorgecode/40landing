from django.core.management.base import BaseCommand
from pages.models import Page
import random

class Command(BaseCommand):
    help = 'Generate 40 unique, high-intent meta titles using your 65+ keywords'

    def handle(self, *args, **kwargs):
        # List of purchase-intent-based titles from your keyword list
        meta_titles = [
            "Best Website Builder for Small Business",
            "Build Your Own Website – DIY your own website",
            "Create a Website for Your Business",
            "Business Website Builder – Easy & Fast",
            "Website Design for Company – Launch Fast",
            "Responsive Website Templates for SMBs",
            "Easy Website Builder for Founders",
            "Simple Website Builder for Local Shops",
            "Top Website Builder for Entrepreneurs",
            "Web Design Services for Small Businesses",
            "Professional HTML Website Template",
            "Modern Website Design – Ready to Deploy",
            "Functional Website Template – Download & Go",
            "Django Web Template – Easy Setup",
            "Best Site Builder for Local Businesses",
            "Best Web Builder for Small Business",
            "Online Presence Starter – No Coding",
            "Start Your Business Website Today",
            "Perfect Website Template for SMBs",
            "Skip Manual Setup – Get Started Fast",
            "No Developer Needed – I will help you set it up",
            "HTML & CSS Website Template – Ready to Go",
            "Launch Your Company Site in Minutes",
            "Small Business Website Design Service",
            "Build a Site Without Coding Required",
            "Best Website Maker for Entrepreneurs",
            "Professional Web Template for Founders",
            "Functional HTML Template for Companies",
            "Website Creation Sites – Start Today",
            "Responsive Website – Skip the Boring Part",
            "Build Your Online Presence – Fast Setup",
            "Easy-to-Customize Web Template",
            "Local Business Website – Instant Access",
            "Website Development Made Simple",
            "Download, Build & Launch – Best Web Template",
            "Founders' Choice – Business Website",
            "Best HTML Template for Local Companies",
            "Web Design Company Alternative – Save Time",
            "Start Fast – Functional Business Site",
            "Business Website Creator – Just Add Brand"
        ]

        # Descriptions that match buyer intent
        meta_descriptions = [
            "A fully working Django website template. Setup in under 20 minutes.",
            "Best website builder for small businesses – Minimal development skill needed.",
            "Professional HTML site you can download and launch fast.",
            "Responsive web design included – works on mobile & desktop.",
            "Business website builder – start where others begin.",
            "Create a website for your business – easy customization.",
            "Modern layout – just edit content and go live.",
            "Functional template with contact form + admin panel.",
            "Perfect for SMBs looking to build online presence.",
            "Easy setup – no coding required – just customize.",
            "Skip manual setup – launch your site in minutes.",
            "Django-powered. Ready to deploy. Easy to update.",
            "Local business or service provider? Start with this template.",
            "No dev experience? No problem – 30 day free IT support",
            "Build your own website – no third-party tools needed.",
            "Launch today – professional design out of the box.",
            "Small business website – built fast. Looks great.",
            "Simple website builder for entrepreneurs and founders.",
            "Start fast – responsive templates ready to deploy.",
            "Customizable HTML template for company websites.",
            "Best way to create a website without hiring a dev.",
            "Ideal for non-tech users who need a professional site.",
            "Built-in contact form – collect leads right away.",
            "Just add brand – then launch your business website.",
            "HTML & CSS template – modern design, easy changes.",
            "Skip the boring part – get started instantly.",
            "Website creation sites don’t match this quality.",
            "Ready-to-use web template – no extra plugins.",
            "Fast deployment – ideal for local shops & services.",
            "Best alternative to DIY website builders.",
            "Clean codebase – customize without developer help.",
            "Start your online presence – no learning curve.",
            "Perfect for startups needing a simple business site.",
            "Top-rated Django website starter – trusted by founders.",
            "Easy web builder – looks professional out of the box.",
            "Download. Customize. Go live – no monthly fees.",
            "Professional web design for small businesses.",
            "Business owners: Build your site without dev work.",
            "Best HTML template for quick website launches.",
            "Save time building your online presence.",
        ]

        # Update each page with unique title/description
        pages = Page.objects.all().order_by('id')[:40]
        used_titles = set()

        updated_count = 0

        for idx, page in enumerate(pages):
            # Make sure we don’t reuse titles
            title = None
            while len(used_titles) < len(meta_titles):
                title = random.choice(meta_titles)
                if title not in used_titles:
                    used_titles.add(title)
                    break

            # If we run out of unique titles (shouldn't happen with 40 entries)
            if not title and idx < len(meta_titles):
                title = meta_titles[idx % len(meta_titles)]

            page.meta_title = title
            page.meta_description = random.choice(meta_descriptions)
            page.save()
            updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Updated {updated_count} landing pages with unique, intent-driven meta titles"))