from django.core.management.base import BaseCommand
from hw2app.models import Client

class Command(BaseCommand):
    help = 'Get all clients.'
    
    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'ID {client.pk}, Имя: {client.name}, Email: {client.email}, Phone: {client.phone}, Address: {client.address}.')
            