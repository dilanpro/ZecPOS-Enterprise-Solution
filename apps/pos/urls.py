from django.urls import path

from . import views

urlpatterns = [
    path("", views.PosDashboardView.as_view(), name="pos"),
]
