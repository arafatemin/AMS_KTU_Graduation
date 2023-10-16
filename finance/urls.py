from django.urls import path
from .views import *


urlpatterns = [
    path('income', income_view, name='income'),
]