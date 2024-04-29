from django.core.management.base import BaseCommand
from hw2app.models import Client

class Command(BaseCommand):
    help = 'Add new client in DB'
    
    def handle(self, *args, **kwargs):
        client = Client(
            name = 'Костя',
            email = 'example@mail.ru',
            phone = '+7(978)001-25-14',
            address = 'Moscow'
        )
        if Client.objects.filter(email=client.email).exists():
            self.stdout.write(f'Клиент с данным email: {client.email}, уже создан.')
            return
        client.save()
        self.stdout.write(f'Клиент: {client.name}, email: {client.email} успешно создан.')