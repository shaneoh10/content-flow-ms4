from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.PostView.as_view(), name='posts'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post',
         login_required(views.AddPostView.as_view()), name='add_post'),
    path('edit_post/<int:pk>',
         login_required(views.EditPostView.as_view()), name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('category/<str:cat>/', views.category_view, name='category'),
    path('like_post/<int:pk>', views.like_post_view, name='like_post'),
]
