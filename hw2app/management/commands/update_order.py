from django.core.management.base import BaseCommand
from hw2app.models import Order, Product


class Command(BaseCommand):
    help = 'Update order.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Orger ID')
        parser.add_argument('quantity', type=int, help='Quantity Product')
        parser.add_argument('product', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        quantity = kwargs.get('quantity')
        product = kwargs.get('product')
        order = Order.objects.filter(pk=pk).first()
        product = Product.objects.filter(pk=product).first()
        if order is not None and product is not None:
            order.quantity = quantity
            order.total_price = product.price * quantity
            order.save()
            order.product.clear()
            order.product.add(product)
            self.stdout.write(f'Заказ {pk} изменен!')
        else:
            self.stdout.write('Заказ или товар не найден')