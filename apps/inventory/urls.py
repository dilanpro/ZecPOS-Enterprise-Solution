from django.urls import path

from . import views

urlpatterns = [
    # Product Endpoints
    path("", views.ProductsDashboardView.as_view(), name="products"),
    # Category Endpoints
    path("categories", views.CategoriesDashboardView.as_view(), name="categories"),
    path(
        "categories-search",
        views.CategorySearchView.as_view(),
        name="categories-search",
    ),
    path(
        "categories/create",
        views.CategoryCreateView.as_view(),
        name="categories-create",
    ),
    path(
        "categories/<int:category_id>/edit",
        views.CategoryEditView.as_view(),
        name="categories-edit",
    ),
    # Supplier Endpoints
    path("suppliers", views.SuppliersDashboardView.as_view(), name="suppliers"),
    path(
        "suppliers-search", views.SupplerSearchView.as_view(), name="suppliers-search"
    ),
    path(
        "suppliers/create", views.SupplierCreateView.as_view(), name="suppliers-create"
    ),
    path(
        "suppliers/<int:supplier_id>/edit",
        views.SupplierEditView.as_view(),
        name="suppliers-edit",
    ),
]
