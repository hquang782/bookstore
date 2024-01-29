from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cart

# Assume you have a Product model with fields like 'name', 'price', etc.


def view_cart(request):
    # Xử lý hiển thị giỏ hàng của người dùng
    # Lấy giỏ hàng của người dùng từ session
    cart = request.session.get("cart", {})

    # Lấy thông tin sản phẩm từ database dựa trên product_id trong giỏ hàng
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        subtotal = product.price * quantity
        total_price += subtotal
        cart_items.append(
            {"product": product, "quantity": quantity, "subtotal": subtotal}
        )

    return render(
        request,
        "./components/cart/view_cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


def add_to_cart(request, product_id):
    # Xử lý thêm sản phẩm vào giỏ hàng
    if "cart" not in request.session:
        # Nếu chưa có giỏ hàng, tạo một giỏ hàng mới
        request.session["cart"] = {}

    cart = request.session["cart"]

    if product_id in cart:
        # Nếu sản phẩm đã có trong giỏ hàng, tăng số lượng lên 1
        cart[product_id] += 1
    else:
        # Nếu sản phẩm chưa có trong giỏ hàng, thêm vào giỏ hàng với số lượng là 1
        cart[product_id] = 1

    # Lưu lại giỏ hàng vào session
    request.session["cart"] = cart

    return redirect("view_cart")  # Chuyển hướng về trang hiển thị giỏ hàng


def remove_from_cart(request, product_id):
    # Xử lý xóa sản phẩm khỏi giỏ hàng
    cart = request.session.get("cart", {})

    if product_id in cart:
        # Nếu sản phẩm có trong giỏ hàng, xóa nó khỏi giỏ hàng
        del cart[product_id]

    # Lưu lại giỏ hàng vào session
    request.session["cart"] = cart

    return redirect("view_cart")
