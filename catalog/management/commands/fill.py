from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        categories_for_add = [
            {'name': 'Rat', 'description': 'Running and laugh'},
            {'name': 'Tree', 'description': 'Green'}
        ]
        categories = []
        for category in categories_for_add:
            categories.append(Category(**category))

        Category.objects.bulk_create(categories)
