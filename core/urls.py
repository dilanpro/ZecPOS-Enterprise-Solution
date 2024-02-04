from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("sa/", include("apps.super_admin.urls")),
    path("auth/", include("apps.user.urls")),
    path("pos/", include("apps.pos.urls")),
]
