from django.contrib import admin

from catalog.forms import ProductAdminForm
from catalog.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description',]
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}
    
    def save_model(self, request, obj, form, change):
        obj.save(using='mongodb')

    def get_queryset(self, request):
        return Product.objects.using('mongodb')

admin.site.register(Product, ProductAdmin) 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', )
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    exclude = ('created_at', 'updated_at',)

    prepopulated_fields = {'slug':('name',)}

    def save_model(self, request, obj, form, change):
        obj.save(using='mongodb')

    def get_queryset(self, request):
        return Category.objects.using('mongodb')
admin.site.register(Category, CategoryAdmin)