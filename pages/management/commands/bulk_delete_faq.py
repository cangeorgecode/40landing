from django.core.management.base import BaseCommand
from pages.models import FAQ

class Command(BaseCommand):
    help = 'Delete specific FAQs by question'

    def handle(self, *args, **kwargs):
        questions_to_delete = [
            "What license do I get?",
            "Will this work for my local business?"
        ]

        for question in questions_to_delete:
            deleted_count = FAQ.objects.filter(question=question).delete()
            self.stdout.write(self.style.SUCCESS(f"🗑️ Deleted '{question}' – {deleted_count[0]} entries"))

        self.stdout.write(self.style.SUCCESS("✅ All targeted FAQs removed"))