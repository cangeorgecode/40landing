from django.core.management.base import BaseCommand
from pages.models import FAQ

class Command(BaseCommand):
    help = 'Update the answer to "Do I need any developer experience?"'

    def handle(self, *args, **kwargs):
        question = "How long does setup take?"
        new_answer = "Under 20 minutes. Download the files, install the dependencies, and launch!"

        updated_count = FAQ.objects.filter(question=question).update(answer=new_answer)

        self.stdout.write(self.style.SUCCESS(f"✅ Updated {updated_count} FAQ entries"))