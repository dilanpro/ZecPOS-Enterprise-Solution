from django import forms

from core.forms import FormFirstErrorTrackingMixin

from .models import Category, Product, Supplier, Item


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
