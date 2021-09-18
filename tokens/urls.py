from django.urls import path
from . import views

urlpatterns = [
    path('', views.tokens, name='tokens'),
    path('checkout', views.token_checkout, name='token_checkout'),
    path('send_reward/<str:receiver>', views.send_reward, name='send_reward'),
]
