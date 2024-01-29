from django.db import models
from django.urls import reverse
from catalog.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Unique value for category page URL, created from name.",
    )
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    quantity = models.IntegerField()
    old_price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, default=0.00
    )
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meta_keywords = models.CharField(
        max_length=255, help_text="Comma-delimited set of SEO keywords for meta tag"
    )
    meta_description = models.CharField(
        max_length=255, help_text="Content for description meta tag"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
    @property
    def get_absolute_url(self):
        return reverse('catalog_product', kwargs={'category_slug': self.slug})
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None 


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
