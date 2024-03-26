from django import forms

from core.forms import FormFirstErrorTrackingMixin

from .models import GRN, Category, GRNItem, Product, Supplier


class SupplierForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    class Meta:
        model = Supplier
        fields = [
            "name",
            "contact_name",
            "contact_email",
            "contact_phone",
            "website",
            "address_line_1",
            "address_line_2",
            "city",
            "postal_code",
        ]


class CategoryForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    class Meta:
        model = Category
        fields = [
            "title",
        ]


class ProductForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ["title", "category"]


class GRNCreateEditForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    class Meta:
        model = GRN
        fields = ["title", "special_note"]


class GRNDiscountsForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    class Meta:
        model = GRN
        fields = ["flat_discount", "percentage_discount"]


class GRNItemsForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    class Meta:
        model = GRNItem
        fields = [
            "product",
            "opening_quantity",
            "price",
            "cost",
            "discount_flat_on_total",
            "discount_flat_on_single_item",
            "discount_percentage",
            "discount_free_items",
        ]
