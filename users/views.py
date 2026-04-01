from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # автоматически логиним
            # Редирект в зависимости от роли
            if user.role == 'buyer':
                return redirect('buyer_dashboard')  # пока можно создать пустой шаблон
            elif user.role == 'seller':
                return redirect('seller_dashboard')
            else:
                return redirect('buyer_dashboard')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def buyer_dashboard(request):
    if request.user.role != 'buyer':
        return redirect('seller_dashboard')  # или на главную
    return render(request, 'users/buyer_dashboard.html')


@login_required
def seller_dashboard(request):
    if request.user.role != 'seller':
        return redirect('buyer_dashboard')  # или на главную
    return render(request, 'users/seller_dashboard.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # если используем username
        if user is not None:
            login(request, user)
            # редирект по роли
            if user.role == 'buyer':
                return redirect('buyer_dashboard')
            elif user.role == 'seller':
                return redirect('seller_dashboard')
        else:
            messages.error(request, 'Неверный email или пароль')
    return render(request, 'users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')  # или на главную страницу
