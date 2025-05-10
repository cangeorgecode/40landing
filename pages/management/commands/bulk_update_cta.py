from django.core.management.base import BaseCommand
from pages.models import Section

class Command(BaseCommand):
    help = "Remove 'Over 50 happy developers' from all Final CTA sections"

    def handle(self, *args, **kwargs):
        # Filter only 'final_cta' sections
        cta_sections = Section.objects.filter(section_type='final_cta')

        for section in cta_sections:
            if 'Over 50 happy developers' in section.content:
                section.content = section.content.replace('Over 50 happy developers\n', '')
                section.save()
                self.stdout.write(f"Updated {section.page.title}")

        self.stdout.write(self.style.SUCCESS("✅ Removed text from all final CTA sections"))