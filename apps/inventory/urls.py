from django.urls import include, path

from .views import categories, grn_items, grns, products, suppliers

product_urlpatterns = [
    path("", products.ProductsDashboardView.as_view(), name="products"),
    path("search", products.ProductSearchView.as_view(), name="products-search"),
    path("create", products.ProductCreateView.as_view(), name="products-create"),
    path(
        "<int:product_id>/action",
        products.ProductsActionView.as_view(),
        name="products-action",
    ),
    path(
        "<int:product_id>/edit",
        products.ProductEditView.as_view(),
        name="products-edit",
    ),
    path(
        "<int:product_id>/grns",
        products.ProductsRelatedGRNItemsView.as_view(),
        name="products-related-grns",
    ),
    path(
        "<int:product_id>/mark-price-change",
        products.ChangeMarkPriceView.as_view(),
        name="products-mark-price-change",
    ),
]

categories_urlpatterns = [
    path("", categories.CategoriesDashboardView.as_view(), name="categories"),
    path(
        "search",
        categories.CategorySearchView.as_view(),
        name="categories-search",
    ),
    path(
        "<int:category_id>/action",
        categories.CategoriesActionView.as_view(),
        name="categories-action",
    ),
    path(
        "create",
        categories.CategoryCreateView.as_view(),
        name="categories-create",
    ),
    path(
        "<int:category_id>/edit",
        categories.CategoryEditView.as_view(),
        name="categories-edit",
    ),
]

suppliers_urlpatterns = [
    path("", suppliers.SuppliersDashboardView.as_view(), name="suppliers"),
    path(
        "<int:supplier_id>/action",
        suppliers.SuppliersActionView.as_view(),
        name="suppliers-action",
    ),
    path(
        "search",
        suppliers.SupplerSearchView.as_view(),
        name="suppliers-search",
    ),
    path(
        "create",
        suppliers.SupplierCreateView.as_view(),
        name="suppliers-create",
    ),
    path(
        "<int:supplier_id>/edit",
        suppliers.SupplierEditView.as_view(),
        name="suppliers-edit",
    ),
]

grn_urlpatterns = [
    path(
        "<int:supplier_id>",
        grns.GRNDashboardView.as_view(),
        name="grns",
    ),
    path(
        "<int:supplier_id>/search",
        grns.GRNSearchView.as_view(),
        name="grn-search",
    ),
    path(
        "<int:grn_id>/action",
        grns.GRNActionView.as_view(),
        name="grn-action",
    ),
    path(
        "<int:grn_id>/finalize",
        grns.GRNFinalizeView.as_view(),
        name="grn-finalize",
    ),
    path(
        "suppliers/<int:supplier_id>/create",
        grns.GRNCreateView.as_view(),
        name="grn-create",
    ),
    path(
        "<int:grn_id>/edit",
        grns.GRNEditView.as_view(),
        name="grn-edit",
    ),
    path(
        "<int:grn_id>/discounts",
        grns.GRNDiscountsView.as_view(),
        name="grn-discounts",
    ),
    path(
        "<int:grn_id>/delete",
        grns.GRNDeleteView.as_view(),
        name="grn-delete",
    ),
]


grn_items_urlpatterns = [
    path(
        "grn/<int:grn_id>/create",
        grn_items.GRNItemCreateView.as_view(),
        name="grn-items-create",
    ),
    path(
        "grn/<int:grn_id>/grn-item/<int:grn_item_id>/clone",
        grn_items.GRNItemCloneView.as_view(),
        name="grn-items-clone",
    ),
    path(
        "grn/<int:grn_id>/grn-item/<int:grn_item_id>/edit",
        grn_items.GRNItemEditView.as_view(),
        name="grn-items-edit",
    ),
    path(
        "grn/<int:grn_id>/grn-item/<int:grn_item_id>/delete",
        grn_items.GRNItemDeleteView.as_view(),
        name="grn-items-delete",
    ),
]

urlpatterns = [
    path("products/", include(product_urlpatterns)),
    path("categories/", include(categories_urlpatterns)),
    path("suppliers/", include(suppliers_urlpatterns)),
    path("grn/", include(grn_urlpatterns)),
    path("grn-items/", include(grn_items_urlpatterns)),
]
