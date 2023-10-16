from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('loginout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('setting/', setting_view, name='setting'),
]