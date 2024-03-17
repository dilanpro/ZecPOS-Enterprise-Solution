from django.db import models

from apps.user.models import Business, User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    # Meta Info
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="categories"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categories"
    )


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    # Meta Info
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="products"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products"
    )


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)

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

    # Meta Info
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="suppliers"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="suppliers"
    )


class Item(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name="items"
    )

    # Price Info
    price = models.FloatField(default=0)
    cost = models.FloatField(default=0)

    # Stocks
    quantity = models.FloatField(default=0)

    # Meta Info
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="items"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
