from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    icon_url = models.CharField(max_length=200, default="")
    tokens = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    display_price = models.FloatField(default=0)

    def __str__(self):
        return self.name
