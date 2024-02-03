from django import forms

from core.forms import FormFirstErrorTrackingMixin
from .models import Business, User


class BusinessForm(FormFirstErrorTrackingMixin, forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            "title",
            "status",
            "renewal_date",
            "seat_count",

            "contact_name",
            "contact_email",
            "contact_phone",
            "website",

            "address_line_1",
            "address_line_2",
            "city",
            "postal_code",
        ]


class UserCreateForm(FormFirstErrorTrackingMixin, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "name",
            "role",
        ]

