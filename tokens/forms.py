from django import forms
from .models import Order, Withdrawal


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("card_name", "username", "email", "tokens", "order_total")


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = (
            "account_name",
            "iban",
            "username",
            "email",
            "tokens",
            "withdrawal_total",
        )
