from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name="posts"),
    path('<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('add_post', views.AddPostView.as_view(), name="add_post"),
]
