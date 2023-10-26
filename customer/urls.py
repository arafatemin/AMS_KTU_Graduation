from django.urls import path
from .views import *

urlpatterns = [
    path('customerView', customer_view, name='customerView'),
    path('customerCreate', customer_create_view, name='customerCreate'),
    path('customerUpdate/<int:pk>', customer_update_view, name='customerUpdate'),
    path('customerDelete/<int:pk>', customer_delete_view, name='customerDelete'),
    path('customerDetail/<int:pk>', customer_details_view, name='customerDetail'),

    ]