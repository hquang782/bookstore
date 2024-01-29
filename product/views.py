# product/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product


def view_product(request, product_id):
    # Xử lý hiển thị chi tiết sản phẩm
    product = get_object_or_404(Product, pk=product_id)
    return render(
        request, "./components/products/view_product.html", {"product": product}
    )


def list_products(request):
    # Xử lý hiển thị danh sách sản phẩm
    products = Product.objects.all()
    return render(
        request, "./components/products/product_list.html", {"products": products}
    )
