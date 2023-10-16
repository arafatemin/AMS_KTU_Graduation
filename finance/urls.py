from django.urls import path
from .views import *

urlpatterns = [
    path('income', income_view, name='income'),
    path('income_create', income_create_view, name='income_create'),
    path('income_update/<int:pk>', income_update_view, name='income_update'),
    path('income_delete/<int:pk>', income_delete_view, name='income_delete'),

    path('income_category', income_category_view, name='income_category'),
    path('income_category_create', income_category_create_view, name='income_category_create'),
    path('income_category_update/<int:pk>', income_category_update_view, name='income_category_update'),
    path('income_category_delete/<int:pk>', income_category_delete_view, name='income_category_delete'),

    path('outcome', outcome_view, name='outcome'),
    path('outcome_create', outcome_create_view, name='outcome_create'),
    path('outcome_update/<int:pk>', outcome_update_view, name='outcome_update'),
    path('outcome_delete/<int:pk>', outcome_delete_view, name='outcome_delete'),


    path('outcome_category', outcome_category_view, name='outcome_category'),
    path('outcome_category_create', outcome_category_create_view, name='outcome_category_create'),
    path('outcome_category_update/<int:pk>', outcome_category_update_view, name='outcome_category_update'),
    path('outcome_category_delete/<int:pk>', outcome_category_delete_view, name='outcome_category_delete'),
]
