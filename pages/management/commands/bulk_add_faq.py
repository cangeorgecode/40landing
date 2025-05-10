from django.core.management.base import BaseCommand
from pages.models import Page, FAQ

class Command(BaseCommand):
    help = 'Add universal FAQs to all landing pages'

    def handle(self, *args, **kwargs):
        default_faqs = [
            {
                "question": "Do I need any developer experience?",
                "answer": "No! The site is fully functional out of the box. You can clone it, change text/images, and go live without coding."
            },
            {
                "question": "How long does setup take?",
                "answer": "Under 20 minutes. Just clone the repo, install dependencies, and deploy."
            },
            {
                "question": "Can I customize the design?",
                "answer": "Yes – built with Tailwind CSS + DaisyUI, so you can easily tweak colors, layout, fonts, and more."
            },
            {
                "question": "Is there support after purchase?",
                "answer": "Yes – free email support for 30 days to help you get started."
            },
            {
                "question": "What license do I get?",
                "answer": "Developer-only license – you can use it for yourself or client work, but not redistribute or resell the template itself."
            },
            {
                "question": "Can I host this anywhere?",
                "answer": "Yes – it's a standard Django app. Works on Linode, Render, Heroku, Vercel, or any Python-friendly platform."
            },
            {
                "question": "Will this work for my local business?",
                "answer": "Absolutely – many users have used it for shops, service providers, consultants, and freelancers."
            }
        ]

        pages = Page.objects.all()
        total_pages = pages.count()

        for idx, page in enumerate(pages):
            # Delete existing FAQs first (optional)
            page.faqs.all().delete()

            for order, entry in enumerate(default_faqs):
                FAQ.objects.create(
                    page=page,
                    question=entry["question"],
                    answer=entry["answer"],
                    order=order
                )

            self.stdout.write(f"✅ Added FAQs to {page.title}")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 FAQs added to {total_pages} landing pages"))