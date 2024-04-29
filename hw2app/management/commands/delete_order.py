from django.core.management.base import BaseCommand
from hw2app.models import Order


class Command(BaseCommand):
    help = 'Delete ORder by ID'

    def add_arguments(self,parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        product = order.product.first()
        if order is not None:
            if input(f'Заказ: {order.pk}, Товар: {product}, Сумма заказа: {order.total_price}. \n Вы уверены, что хотите удалить заказ с: {pk}? press button (y - for YES, n - for NO) ') == 'y':
                order.delete()
                self.stdout.write(f'Заказ c {pk} удален!')
            else:
                self.stdout.write(f'Заказ c {pk} не удален!')
        else:
            self.stdout.write(f'Заказ c {pk} не найден')