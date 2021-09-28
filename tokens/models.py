import uuid
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    icon_url = models.CharField(max_length=200, default="")
    tokens = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    display_price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    card_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    tokens = models.IntegerField(null=False, blank=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """
        Generate random order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override original save method to set order number
        if no order number is set
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
