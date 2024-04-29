from django.core.management.base import BaseCommand
from hw2app.models import Client

class Command(BaseCommand):
    help = 'Delete client by emailaddress'
    
    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email by client')
        
    def handle(self, *args, **kwargs):
        email = kwargs.get('email')
        client = Client.objects.filter(email=email).first()
        if client:
            if input(f'Удалить клиента с: {email}? press button (y - for YES, n - for NO)') == 'y':
                client.delete()
                self.stdout.write(f'Клиент с {email} удален.')
            else:
                self.stdout.write(f'Клиент c {email} не удален.')
        else:
            self.stdout.write(f'Клиент с {email} не существует.') 
            