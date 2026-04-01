from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('seller/', views.seller_dashboard, name='seller_dashboard'),
    path('logout/', views.user_logout, name='logout'),
]
