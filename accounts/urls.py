from django.urls import path, include
from .views import get_login, register_seller

urlpatterns= [
    path('login/', get_login, name='login'),
    path('login/seller', register_seller, name='register_seller')
    ]