from django.core.management.base import BaseCommand
from pages.models import Page, Section

import random

class Command(BaseCommand):
    help = 'Bulk update all landing pages with persona-driven content'

    def handle(self, *args, **kwargs):
        # Define the 4 buyer personas
        personas = {
            'smb': {
                'headlines': [
                    "Professional Business Website Template",
                    "Functional Site for SMBs – Ready to Deploy",
                    "Best Website Builder for Small Businesses",
                    "Premium HTML Template for Local Companies",
                    "Perfect Website for Service Providers",
                    "Business Website You Can Clone & Customize",
                    "Modern Design – No Dev Needed",
                    "Easy-to-Use Web Template for Entrepreneurs",
                    "Responsive Website for Your Small Business",
                    "Start Fast – Functional Out of the Box"
                ],
                'subheadlines': [
                    "A fully functional website built with Django. Setup in under 20 minutes.",
                    "No developer experience needed. Just clone, customize, and go live.",
                    "Built for small businesses looking for a professional online presence.",
                    "Includes working contact form + admin panel + beautiful layout.",
                    "Perfect for local shops, consultants, and service-based businesses.",
                    "Ready to deploy on Linode, Render, or Vercel – no extra work.",
                    "Clean codebase – easy to customize even if you're not a dev.",
                    "Start with a solid foundation – skip the boring setup work.",
                    "Django backend included – manage content from day one.",
                    "Beautiful UX out of the box – no design skills required."
                ],
                'ctas': [
                    ("Download Now – Start Customizing", "/checkout/"),
                    ("Buy Now – Launch Today", "/checkout/"),
                    ("Instant Access – No Dev Needed", "/checkout/"),
                    ("Start Building – No Coding Required", "/checkout/"),
                    ("Skip Setup – Get Started Fast", "/checkout/")
                ]
            },
            'founder': {
                'headlines': [
                    "Launch Your Website in Minutes",
                    "Clone, Customize, Go Live – Fast",
                    "Founders' Choice – Skip Manual Setup",
                    "Functional Template for Indie Hackers",
                    "Build Faster – No Developer Needed",
                    "Start with a Working Foundation",
                    "Website That’s Ready to Go",
                    "No More Boilerplate Code",
                    "Pre-Built Django Template",
                    "From Zero to Online in 20 Minutes"
                ],
                'subheadlines': [
                    "A fully working template – just clone, edit, and go live.",
                    "Designed for founders who want speed over complexity.",
                    "Includes contact form + responsive layout + admin panel.",
                    "No need to build from scratch – start where others begin.",
                    "Skip the boring part – focus on what matters most.",
                    "Django-powered – easy to deploy and maintain.",
                    "Perfect for side projects, MVPs, or passion projects.",
                    "Just drop it into your project – no setup needed.",
                    "Great for non-devs who still want control.",
                    "Start with a solid foundation – not an empty file."
                ],
                'ctas': [
                    ("Get Started Now – Save 10+ Hours", "/checkout/"),
                    ("Skip Setup – Build Faster", "/checkout/"),
                    ("Start With a Working Template", "/checkout/"),
                    ("Launch Today – No Dev Needed", "/checkout/"),
                    ("Download Now – Instant Access", "/checkout/")
                ]
            },
            'agency': {
                'headlines': [
                    "Django-Powered Website Template for Clients",
                    "Deliver Websites Faster – Pre-Built Design",
                    "For Agencies & Freelancers – Ready to Use",
                    "Client-Friendly Django Templates",
                    "HTML Template with Admin Panel Included",
                    "Best Web Template for Client Projects",
                    "Tailored for Agencies – Fully Functional",
                    "Web Design Made Easier with This Template",
                    "Top Template for Web Developers",
                    "Quick Setup for Multiple Builds"
                ],
                'subheadlines': [
                    "Premium HTML design with Tailwind CSS + DaisyUI",
                    "Contact form ready – no extra coding needed",
                    "Django backend for easy customization",
                    "Perfect for agencies building client sites",
                    "Fast deployment – ideal for multiple clients",
                    "Modern layout that works across devices",
                    "No dev team? No problem – just plug and play",
                    "Fully working admin panel included",
                    "Save time when building websites",
                    "Start with a working foundation"
                ],
                'ctas': [
                    ("Buy Now – For Client Work", "/checkout/"),
                    ("Start Delivering Faster", "/checkout/"),
                    ("Instant Access – Perfect for Teams", "/checkout/"),
                    ("Get Started – For Agency Use", "/checkout/"),
                    ("Download for Client Project", "/checkout/")
                ]
            },
            'diy': {
                'headlines': [
                    "Build Your Own Website – No Developer Needed",
                    "DIY Business Website – Easy to Set Up",
                    "Start Fast – Functional Template",
                    "No Dev Experience Required",
                    "Create Your Site in Under 20 Minutes",
                    "Simple Website Builder for Founders",
                    "Your First Website Starts Here",
                    "Easy Django Template for Non-Coders",
                    "Customize Without Coding",
                    "Start Your Online Presence Today"
                ],
                'subheadlines': [
                    "No coding required – just clone and edit.",
                    "Fully working contact form included.",
                    "Modern, responsive design – looks great on any device.",
                    "Set up in under 20 minutes.",
                    "Django backend so you can manage content.",
                    "Clean code. Easy customization.",
                    "Perfect for first-time site builders.",
                    "All files included – no extra tools needed.",
                    "Just install and launch – no learning curve.",
                    "Best choice for non-developers who want control."
                ],
                'ctas': [
                    ("Start Building Today", "/checkout/"),
                    ("Download Now – Easy Setup", "/checkout/"),
                    ("Launch Your Website in 20 Minutes", "/checkout/"),
                    ("Buy Now – No Dev Needed", "/checkout/"),
                    ("Skip the Boring Part – Clone & Go", "/checkout/")
                ]
            }
        }

        # Split into groups of 10 pages each
        pages = list(Page.objects.all())
        if len(pages) < 40:
            self.stdout.write(self.style.WARNING("⚠️ Less than 40 pages found – using available ones only"))

        chunk_size = 10
        page_chunks = [pages[i:i + chunk_size] for i in range(0, len(pages), chunk_size)]
        persona_keys = list(personas.keys())

        for idx, group in enumerate(page_chunks[:4]):
            persona = persona_keys[idx]
            self.stdout.write(f"🎯 Assigning '{persona}' content to 10 pages...")

            for page in group:
                try:
                    hero = page.sections.get(section_type='hero')
                except Section.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"⚠️ No hero section for {page.title}"))
                    continue

                try:
                    benefits = page.sections.get(section_type='benefits')
                except Section.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"⚠️ No benefits section for {page.title}"))
                    continue

                try:
                    cta = page.sections.get(section_type='final_cta')
                except Section.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"⚠️ No final CTA section for {page.title}"))
                    continue

                # Update Hero
                hero.heading = random.choice(personas[persona]['headlines'])
                hero.content = random.choice(personas[persona]['subheadlines'])
                hero.button_text, hero.button_link = random.choice(personas[persona]['ctas'])
                hero.save()

                # Update Benefits
                benefits.heading = f"Why This Works for {persona.capitalize()}"
                benefits.content = "\n\n".join([
                    "✔️ Functional out of the box",
                    "✔️ Responsive web design",
                    "✔️ Contact form included",
                    "✔️ Django admin panel",
                    "✔️ Easy customization in under 20 minutes"
                ])
                benefits.save()

                # Update Final CTA
                cta.heading = "Still Have Questions?"
                cta.content = "Perfect. We've helped hundreds get their site live fast."
                cta.button_text = "Buy Now – Launch in 20 Minutes"
                cta.button_link = "/checkout/"
                cta.save()

                self.stdout.write(self.style.SUCCESS(f"✅ Updated: {page.title} → {persona}"))

        self.stdout.write(self.style.SUCCESS("\n🎉 All landing pages updated with persona-driven content"))