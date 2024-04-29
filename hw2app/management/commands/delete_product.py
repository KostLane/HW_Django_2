from django.core.management.base import BaseCommand
from hw2app.models import Product

class Command(BaseCommand):
    help = 'Delete product by ID'
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product:
            if input(f'Удалить продукт с: {pk}? press button (y - for YES, n - for NO)') == 'y':
                product.delete()
                self.stdout.write(f'Продукт с {pk} удален.')
            else:
                self.stdout.write(f'Продукт c {pk} не удален.')
        else:
            self.stdout.write(f'Продукт с {pk} не существует.')