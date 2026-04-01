from django.contrib import admin
from .models import Category, Culture, Product

# Регистрация категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Регистрация культур
@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Регистрация продуктов
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'discount', 'quantity', 'created_at')
    list_filter = ('category', 'cultures')
    search_fields = ('name', 'description')