# product/urls.py

from django.urls import path
from .views import view_product, list_products

app_name = "product"

urlpatterns = [
    path("view_product/<int:product_id>/", view_product, name="view_product"),
    path("products/", list_products, name="list_products"),
    # Add more paths if needed
]
