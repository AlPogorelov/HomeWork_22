from django.core.management import BaseCommand

from HomeWork_22.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@exampl.com')
        user.set_password('5288')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

