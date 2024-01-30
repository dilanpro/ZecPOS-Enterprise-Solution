from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("sa/", admin.site.urls),
    path("auth/", include("apps.user.urls")),
]
