from typing import Any
from blog.models import categories
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        categories.objects.all().delete()
        
        cat = ['Sports', 'Technology', 'Science', 'Art', 'Food']
      

        for category_name in cat:
            categories.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))