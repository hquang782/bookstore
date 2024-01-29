from django.urls import path
from .views import remove_from_cart, view_cart, add_to_cart

urlpatterns = [
    path("cart/", view_cart, name="view_cart"),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    # Add more paths if needed
]
