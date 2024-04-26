from django import forms

from core.forms import FormFirstErrorTrackingMixin
from django.core.validators import MinValueValidator
from .models import GRN, Category, GRNItem, Product, Supplier, SR


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


class ChangeMarkPriceForm(FormFirstErrorTrackingMixin, forms.Form):
    new_price = forms.FloatField()


class SRCreateEditForm(FormFirstErrorTrackingMixin, forms.ModelForm):

    quantity = forms.FloatField(validators=[MinValueValidator(0)])
    quantity = forms.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        model = SR
        fields = ["title", "special_note", "quantity", "item_cost"]
