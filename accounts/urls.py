from django.urls import path, include
from .views import login, register_seller, profile, logout

urlpatterns= [
    path('login/', login, name='login'),
    path('login/seller', register_seller, name='register_seller'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    ]