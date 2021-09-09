from django.urls import path
from . import views

urlpatterns = [
    path('tokens', views.tokens, name='tokens')
]
