from django.urls import path
from . import views

urlpatterns = [
    path('', views.tokens, name='tokens'),
    path('success', views.order_success, name='order_success'),
    path('cancel', views.order_cancel, name='order_cancel'),
    path('send_reward/<str:receiver>', views.send_reward, name='send_reward'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
]
