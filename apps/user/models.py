from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class Business(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    onboarding_date = models.DateTimeField(auto_now_add=True)
    renewal_date = models.DateField()
    seat_count = models.IntegerField(default=1)

    # Contact Info
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20)
    website = models.URLField(null=True, blank=True)

    # Location Info
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.title



class User(AbstractUser):

    ROLES = (
        ('AD', 'Admin'),
        ('MN', 'Manager'),
        ('CS', 'Cashier'),
        ('SK', 'Stock Keeper'),
    )


    # Credentials
    username = models.CharField(
        max_length=255, unique=True, validators=[MinLengthValidator(6)]
    )
    password = models.CharField(max_length=128)

    # User Info
    name = models.CharField(max_length=255)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=2, choices=ROLES, default='CS')

    def __str__(self):
        return self.username
