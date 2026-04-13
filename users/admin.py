from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


# Inline для отображения профиля (аватарка и др.)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    inlines = (ProfileInline,)  # подключаем профиль