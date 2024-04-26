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

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
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

    @property
    def available_stock(self):
        return sum([_item.quantity for _item in self.items.filter(quantity__gt=0, is_finalized=True)])  # type: ignore

    @property
    def latest_price(self):
        items = self.items.filter(quantity__gt=0, is_finalized=True).order_by("-id")  # type: ignore
        if items.exists():
            return items.first().price
        return None

    @property
    def latest_cost(self):
        items = self.items.filter(quantity__gt=0, is_finalized=True).order_by("-id")  # type: ignore
        if items.exists():
            return items.first().actual_cost
        return None

    def __str__(self) -> str:
        return self.title


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


class GRN(models.Model):
    title = models.CharField(max_length=100)
    special_note = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def raw_total_price(self) -> float:
        total = sum([item.total_price for item in self.items.all()])  # type: ignore
        return total

    @property
    def total_price(self) -> float:
        total = sum([item.total_price for item in self.items.all()])  # type: ignore

        # Flat Discount
        total -= self.flat_discount

        # Percentage Discount
        total -= (self.percentage_discount / 100) * total

        return total

    @property
    def discount_flat(self) -> float:
        return self.flat_discount

    @property
    def discount_percentage(self) -> float:
        return (self.percentage_discount / 100) * self.raw_total_price

    is_finalized = models.BooleanField(default=False)

    # Discounts
    flat_discount = models.FloatField(default=0)
    percentage_discount = models.FloatField(default=0)

    # Meta Info
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="grns"
    )
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="grns"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grns")
    finalized_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="finalized_grns",
        blank=True,
        null=True,
    )

    def finalize(self, finalized_by: User):
        self.is_finalized = True
        self.finalized_by = finalized_by
        self.save()

        for _item in self.items.all():  # type: ignore
            _item.calculate_cost()
            _item.is_finalized = True
            _item.finalized_by = finalized_by
            _item.save()


class GRNItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    grn = models.ForeignKey(
        GRN, on_delete=models.CASCADE, related_name="items", blank=True
    )
    opening_quantity = models.FloatField()
    quantity = models.FloatField()
    actual_cost = models.FloatField(default=0)
    cost = models.FloatField()
    price = models.FloatField()

    @property
    def profit(self) -> float:
        return self.price - self.actual_cost

    @property
    def raw_total_price(self) -> float:
        total = self.cost * self.opening_quantity
        return total

    @property
    def flat_discount_on_total(self) -> float:
        return self.discount_flat_on_total

    @property
    def flat_discount_on_items(self) -> float:
        return self.discount_flat_on_single_item * self.opening_quantity

    @property
    def percentage_discount(self) -> float:
        return (self.discount_percentage / 100) * self.raw_total_price

    @property
    def free_items_discount(self) -> float:
        return self.discount_free_items * self.cost

    @property
    def total_price(self) -> float:
        total = self.cost * self.opening_quantity

        # Flat Discount on Total
        total -= self.discount_flat_on_total

        # Flat Discount on Single Item
        total -= self.discount_flat_on_single_item * self.opening_quantity

        # Percentage Discount
        total -= (self.discount_percentage / 100) * total

        # Free Items
        total -= self.discount_free_items * self.cost

        return total

    is_finalized = models.BooleanField(default=False)

    # Discounts
    discount_flat_on_total = models.FloatField(default=0)
    discount_flat_on_single_item = models.FloatField(default=0)
    discount_percentage = models.FloatField(default=0)
    discount_free_items = models.FloatField(default=0)

    # Meta Info
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="items"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    finalized_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="finalized_grn_items",
        blank=True,
        null=True,
    )

    def calculate_cost(self):
        self.actual_cost = self.total_price / self.opening_quantity


class SR(models.Model):
    title = models.CharField(max_length=100)
    special_note = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    quantity = models.FloatField()
    item_cost = models.FloatField()

    @property
    def total_cost(self) -> float:
        return self.quantity * self.item_cost

    # Meta Info
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="srs")
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="srs")
    grn_item = models.ForeignKey(
        GRNItem, on_delete=models.CASCADE, related_name="srs", blank=True, null=True
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="srs")
    finalized_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="finalized_srs",
        blank=True,
        null=True,
    )
