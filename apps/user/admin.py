from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Business, User


class UserAdminModal(UserAdmin):
    list_display = ("username", "name", "business")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("name", "business", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "name",
                    "business",
                    "role",
                ),
            },
        ),
    )


class BusinessAdminModal(admin.ModelAdmin):
    model = Business
    list_display = ("title", "status", "renewal_date", "city")


admin.site.register(User, UserAdminModal)
admin.site.register(Business, BusinessAdminModal)
