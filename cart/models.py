from django.db import models
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartProduct")
    created_at = models.DateTimeField(auto_now_add=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
