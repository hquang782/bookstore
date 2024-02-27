from decimal import Decimal
from django.db import models

from catalog.models import Product

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    product_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def get_product(self):
        try:
            product = Product.objects.using('mongodb').get(id=self.product_id)
            return product
        except Product.DoesNotExist:
            return None
    
    def total(self):
        return self.quantity*Decimal(str(self.get_product().price))
    
    def name(self):
        return self.get_product().name
    
    def price(self):
        return Decimal(str(self.get_product().price))
    
    def get_absolute_url(self):
        product = self.get_product()
        if product:
            return product.get_absolute_url()
        return '#'
    
    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()