from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seller/products/', views.seller_products, name='seller_products'),
]