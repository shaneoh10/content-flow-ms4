from django.contrib import admin
from .models import Product, Order, Withdrawal

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Withdrawal)
