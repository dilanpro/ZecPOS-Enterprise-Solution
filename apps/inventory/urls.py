from django.urls import path

from . import views

urlpatterns = [
    # Product Endpoints
    path("", views.ProductsDashboardView.as_view(), name="products"),
    path("search", views.ProductSearchView.as_view(), name="products-search"),
    path("create", views.ProductCreateView.as_view(), name="products-create"),
    path(
        "<int:product_id>/action",
        views.ProductsActionView.as_view(),
        name="products-action",
    ),
    path(
        "<int:product_id>/edit", views.ProductEditView.as_view(), name="products-edit"
    ),
    # Category Endpoints
    path("categories", views.CategoriesDashboardView.as_view(), name="categories"),
    path(
        "categories-search",
        views.CategorySearchView.as_view(),
        name="categories-search",
    ),
    path(
        "categories/<int:category_id>/action",
        views.CategoriesActionView.as_view(),
        name="categories-action",
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
        "suppliers/<int:supplier_id>/action",
        views.SuppliersActionView.as_view(),
        name="suppliers-action",
    ),
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
    # GRN Endpoints
    path(
        "grn/<int:supplier_id>",
        views.GRNDashboardView.as_view(),
        name="grns",
    ),
    path(
        "grn/<int:supplier_id>/search",
        views.GRNSearchView.as_view(),
        name="grn-search",
    ),
    path(
        "grn/<int:grn_id>/action",
        views.GRNActionView.as_view(),
        name="grn-action",
    ),
    path(
        "grn/<int:grn_id>/finalize",
        views.GRNFinalizeView.as_view(),
        name="grn-finalize",
    ),
    path(
        "grn/create/suppliers/<int:supplier_id>",
        views.GRNCreateView.as_view(),
        name="grn-create",
    ),
    path(
        "grn/<int:grn_id>/edit",
        views.GRNEditView.as_view(),
        name="grn-edit",
    ),
    path(
        "grn/<int:grn_id>/discounts",
        views.GRNDiscountsView.as_view(),
        name="grn-discounts",
    ),
    path(
        "grn/<int:grn_id>/delete",
        views.GRNDeleteView.as_view(),
        name="grn-delete",
    ),
    # GRN Item Endpoints
    path(
        "grn-items/create/grn/<int:grn_id>",
        views.GRNItemCreateView.as_view(),
        name="grn-items-create",
    ),
    path(
        "grn-items/create/grn/<int:grn_id>/grn-item/<int:grn_item_id>",
        views.GRNItemCloneView.as_view(),
        name="grn-items-clone",
    ),
    path(
        "grn-items/create/grn/<int:grn_id>/grn-item/<int:grn_item_id>/edit",
        views.GRNItemEditView.as_view(),
        name="grn-items-edit",
    ),
    path(
        "grn-items/create/grn/<int:grn_id>/grn-item/<int:grn_item_id>/delete",
        views.GRNItemDeleteView.as_view(),
        name="grn-items-delete",
    ),
]
