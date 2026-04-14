from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product

def index(request):
    new_products = Product.objects.order_by('-created_at')[:6]
    return render(request, 'products/index.html', {'new_products': new_products})


@login_required
def seller_products(request):
    if request.user.role != 'seller':
        return redirect('index')

    products = Product.objects.filter(seller=request.user)
    return render(request, 'products/seller_products.html', {'products': products})