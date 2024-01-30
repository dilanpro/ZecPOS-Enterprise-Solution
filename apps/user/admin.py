from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Business, User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'business')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'business', 'is_staff')


class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "contact_name",
        "contact_email",
        "contact_phone",
        "onboading_date",
        "renewal_date",
    )

admin.site.register(User, UserAdmin)
admin.site.register(Business, BusinessAdmin)
