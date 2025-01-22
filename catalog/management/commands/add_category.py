from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category


class Command(BaseCommand):
    help = 'Добавление тестовых продуктов в базу данных'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
