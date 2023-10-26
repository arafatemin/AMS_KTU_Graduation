from django.contrib import admin
from .models import *


class UnitTypeAdmin(admin.ModelAdmin):
    model = UnitType
    list_display = ['name']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']

class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ['title']
    list_display_links = ['title']
    list_per_page = 10
    search_fields = ['title']



class TaxAdmin(admin.ModelAdmin):
    model = Tax
    list_display = ['amount']

    list_per_page = 10
    search_fields = ['amount']



class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'category', 'type', 'quentity', 'staff', 'datetime']
    list_display_links = ['name', 'category', 'type']
    list_editable = ['quentity']
    list_per_page = 10
    search_fields = ['name', 'category', 'type']
    list_filter = ['datetime']



class ProductInStockAdmin(admin.ModelAdmin):
    model = ProductInStock
    list_display = ['product','quantity','user', 'datetime', 'stocks']
    list_display_links = ['product']
    list_editable = ['quantity']
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['product', 'order_quantity', 'staff', 'datetime']
    list_display_links = ['staff', 'product']
    list_per_page = 10

admin.site.register(UnitType, UnitTypeAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Product, ProductAdmin)



admin.site.register(ProductInStock, ProductInStockAdmin)
admin.site.register(Stocks)
admin.site.register(Order, OrderAdmin)
