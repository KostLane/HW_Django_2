from django.core.management.base import BaseCommand
from hw2app.models import Order


class Command(BaseCommand):
    help = "Get order by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')