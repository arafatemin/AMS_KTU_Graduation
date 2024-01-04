from django.urls import path
from .views import *


urlpatterns = [
    path('payment', payment_view, name='payment'),
    path('paymentCreate', payment_create_view, name='paymentCreate'),
    path('paymentUpdate/<int:pk>', payment_update_view, name='paymentUpdate'),
    path('paymentDelete/<int:pk>', payment_delete_view, name='paymentDelete'),


    path('cashMethod', cash_method_view, name='cashMethod'),
    path('bankMethod', bank_method_view, name='bankMethod'),



    path('bank', bank_view, name='bank'),
    path('bankCreate', bank_create_view, name='bankCreate'),
    path('bankUpdate/<int:pk>', bank_update_view, name='bankUpdate'),
    path('bankDelete/<int:pk>', bank_delete_view, name='bankDelete'),
]