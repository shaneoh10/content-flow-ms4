from django.contrib import admin

from .models import Order, Product, Withdrawal

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Withdrawal)
