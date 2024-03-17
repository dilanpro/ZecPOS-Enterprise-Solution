from django import forms

from core.forms import FormFirstErrorTrackingMixin

from .models import Category, Item, Product, Supplier


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
