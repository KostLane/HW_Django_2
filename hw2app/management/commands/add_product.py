from django.core.management.base import BaseCommand
from hw2app.models import Product

class Command(BaseCommand):
    help = 'Add new product.'
    
    def handle(self, *args, **kwargs):
        product = Product(
            name='Vava', 
            description='medical tt a at ', 
            price='3499.99', 
            quantity=30
        )
        product.save()
        self.stdout.write(f'{product}')