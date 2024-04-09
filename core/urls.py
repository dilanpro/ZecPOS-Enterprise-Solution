from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.dashboard.urls")),
    path("sa/", admin.site.urls),
    path("auth/", include("apps.user.urls")),
    path("pos/", include("apps.pos.urls")),
    path("admin/", include("apps.admin_dash.urls")),
    path("inventory/", include("apps.inventory.urls")),
]
