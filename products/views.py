from django.shortcuts import render
from .models import Product

def index(request):
    new_products = Product.objects.order_by('-created_at')[:6]
    return render(request, 'products/index.html', {'new_products': new_products})