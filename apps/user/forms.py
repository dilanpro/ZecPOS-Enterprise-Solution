from django import forms

from core.forms import FormFirstErrorTrackingMixin

from .models import Business, User


def username_validation(value):
    """
    Only allow alphanumeric characters and '_' in the username.
    """
    if not value.replace("_", "").isalnum():
        raise forms.ValidationError(
            "Username must contain only alphanumeric characters."
        )


class BusinessForm(FormFirstErrorTrackingMixin, forms.ModelForm):
    seat_count = forms.IntegerField(min_value=1, label="Seat Count")

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
    username = forms.CharField(
        min_length=6, max_length=15, validators=[username_validation]
    )
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "name",
            "role",
        ]


class UserEditForm(FormFirstErrorTrackingMixin, forms.ModelForm):
    username = forms.CharField(
        min_length=6, max_length=15, validators=[username_validation]
    )

    class Meta:
        model = User
        fields = [
            "username",
            "name",
            "role",
        ]


class UserPasswordResetForm(FormFirstErrorTrackingMixin, forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "password",
        ]
