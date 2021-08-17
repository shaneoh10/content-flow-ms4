from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='posts'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:pk>', views.EditPostView.as_view(), name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]
