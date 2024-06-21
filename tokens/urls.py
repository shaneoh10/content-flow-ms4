from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.tokens, name="tokens"),
    path("send_reward/<str:receiver>", views.send_reward, name="send_reward"),
    path("checkout/<int:pk>", views.checkout, name="checkout"),
    path(
        "checkout_success/<str:order_number>",
        views.checkout_success,
        name="checkout_success",
    ),
    path("wh/", webhook, name="webhook"),
    path("withdrawal", views.withdrawal, name="withdrawal"),
    path(
        "withdrawal_success/<str:order_number>",
        views.withdrawal_success,
        name="withdrawal_success",
    ),
]
