from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='jhhjnx@yandex.ru',
            first_name='Admin',
            last_name='jhhjnx',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123')
        user.save()
