from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "this helps to insert the post data"

    def handle(self, *args: Any, **options: Any):

        Category.objects.all().delete()

        category_list = ["AI", "ML", "Blockchain", "IOT"]

        for category_name in category_list:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))
