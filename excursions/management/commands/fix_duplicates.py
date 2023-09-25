from django.core.management.base import BaseCommand
from excursions.models import Excursions
from django.db.models import Count
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Fix duplicate slugs by making them unique'

    def handle(self, *args, **options):
        # Find records with duplicate slugs
        duplicates = Excursions.objects.values('slug').annotate(count=Count('slug')).filter(count__gt=1)

        # Loop through duplicates and update them
        for duplicate in duplicates:
            excursions = Excursions.objects.filter(slug=duplicate['slug'])
            for i, excursion in enumerate(excursions):
                # Update the slug to make it unique
                excursion.slug = f"{duplicate['slug']}-{i+1}"
                excursion.save()
        self.stdout.write(self.style.SUCCESS('Duplicate slugs have been fixed.'))