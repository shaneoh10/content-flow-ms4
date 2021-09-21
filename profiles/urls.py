from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>', views.user_profile, name='user_profile'),
    path('<str:username>/follow_user/', views.follow_user,
         name='follow_user'),
    path('settings/<str:username>/', views.user_settings, name='user_settings')
]
