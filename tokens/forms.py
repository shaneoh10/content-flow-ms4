from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('card_name', 'username', 'email',
                  'tokens', 'order_total')
