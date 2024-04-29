from django.core.management.base import BaseCommand
from hw2app.models import Order, Client


class Command(BaseCommand):
    help = "Get orders by client ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        orders = Order.objects.filter(client=client)
        if client is not None and orders.exists():
            orders = Order.objects.filter(client=client)
            self.stdout.write(f'{orders}')
        elif client is not None and orders.exists() == False:
            self.stdout.write(f'У клиента {client.name} нет заказов')
        else:
            self.stdout.write('Клиента нет в базе данных')