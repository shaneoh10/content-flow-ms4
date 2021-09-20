from django.urls import path
from . import views

urlpatterns = [
    path('', views.tokens, name='tokens'),
    path('checkout', views.token_checkout, name='token_checkout'),
    path('success', views.order_success, name='order_success'),
    path('cancel', views.order_cancel, name='order_cancel'),
    path('send_reward/<str:receiver>', views.send_reward, name='send_reward'),
    path('create_checkout_session/<pk>', views.CreateCheckoutSession.as_view(),
         name='create_checkout_session'),
]
