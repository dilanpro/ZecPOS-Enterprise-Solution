from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductsDashboardView.as_view(), name="products"),
    path("categories", views.CategoriesDashboardView.as_view(), name="categories"),
    path("suppliers", views.SuppliersDashboardView.as_view(), name="suppliers"),
]
