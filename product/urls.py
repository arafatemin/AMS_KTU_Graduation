from django.urls import path
from product.views import *


urlpatterns = [
    path('productListView', product_list_view, name='productListView'),
    path('productCreate', product_create_view, name='productCreate'),
    path('productDelete/<int:pk>', product_delete_view, name='productDelete'),
    path('productUpdate/<int:pk>', product_update_view, name='productUpdate'),

    path('productCategory', product_category_view, name='productCategory'),
    path('categoryCreate', category_create_view, name='categoryCreate'),
    path('productCategoryUpdate/<int:pk>', product_category_update_view, name='productCategoryUpdate'),
    path('productCategoryDelete/<int:pk>', product_category_delete_view, name='productCategoryDelete'),

    path('productUnit', product_unit_view, name='productUnit'),
    path('unitCreate', unit_create_view, name='unitCreate'),
    path('productUnitUpdate/<int:pk>', product_unit_update_view, name='productUnitUpdate'),
    path('productUnitDelete/<int:pk>', product_unit_delete_view, name='productUnitDelete'),

    path('productTax', product_tax_view, name='productTax'),
    path('taxCreate', tax_create_view, name='taxCreate'),
    path('productTaxUpdate/<int:pk>', product_tax_update_view, name='productTaxUpdate'),
    path('productTaxDelete/<int:pk>', product_tax_delete_view, name='productTaxDelete'),

    path('productInStock', product_stock_view, name='productInStock'),
    path('stockCreateView', stock_create_view, name='stockCreateView'),


    path('staff', staff_view, name='staff'),
    path('staffDetail/<int:pk>', staff_detail_view, name='staffDetail'),
    path('staffUpdate/<int:pk>', staff_update_view, name='staffUpdate'),
    path('staffDelete/<int:pk>', staff_delete_view, name='staffDelete'),

    path('order', order_view, name='order'),
    path('orderCreate', order_Create_view, name='orderCreate'),



]