from django.shortcuts import render, get_object_or_404
from bookstore import settings
from cart import cart
from catalog import search
from catalog.forms import ProductAddToCartForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from catalog.models import Category, Product

def index(request, template_name="catalog/index.html"):
    page_title = 'Home'
    return render(request, template_name, {'page_title': page_title})

def show_category(request, category_slug, template_name="catalog/category.html"):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    page_title = category.name
    return render(request, template_name, {'category': category, 'products': products, 'page_title': page_title})

def show_product(request, product_slug, template_name="catalog/product.html"):
    product = get_object_or_404(Product, slug=product_slug)
    categories = product.categories.using('mongodb')#filter(is_active=True)
    page_title = product.name

    #Kiểm tra phương thức HTTP
    if request.method == 'POST':
        #thêm vào giỏ hàng...tạo form đã bind
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)

        #kiểm tra xem dữ liệu đã post có hợp lệ không
        if form.is_valid():
            #Thêm vào giỏ hàng và chuyển hướng đến giỏ hàng
            cart.add_to_cart(request)
            #Nếu test cookie hoạt động, loại bỏ nó
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = reverse('show_cart')
            return HttpResponseRedirect(url)   
    else:
        #Là GET, tạo form chưa bind. Lưu ý request là một kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')

        #Gán giá trị product_slug cho hidden input
        form.fields['product_slug'].widget.attrs['value'] = product_slug

        #Đặt test cookie trong phần GET đầu tiên
        request.session.set_test_cookie()

    return render(request, template_name, locals() )

def results(request, template_name="catalog/search_result.html"):
    q = request.GET.get('q')
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    matching = search.products(q).get('products')
    paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE)

    try:
        results = paginator.page(page).object_list
    except(InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
    
    page_title = 'Search Results for: ' + q
    return render(request, template_name, locals())