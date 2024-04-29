from django.core.management.base import BaseCommand
from hw2app.models import Product

class Command(BaseCommand):
    help = 'Get all products'
    
    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f'ID {product.pk}, Товар: {product.name}, Описание: {product.description}, Цена: {product.price}, Кол-во товара: {product.quantity}')
        