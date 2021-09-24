from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostView.as_view(), name='posts'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('add_category', views.AddCategoryView.as_view(), name='add_category'),
    path('edit_post/<int:pk>', views.EditPostView.as_view(), name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('category/<str:cat>/', views.category_view, name='category'),
    path('like_post/<int:pk>', views.like_post_view, name='like_post'),
    path('my_feed', views.custom_feed_view, name='my_feed'),
    path('like_comment/<int:pk>', views.like_comment_view,
         name='like_comment'),
    path('<int:pk>/add_comment', views.AddCommentView.as_view(),
         name='add_comment'),
    path('follow_category/<str:cat>', views.follow_category,
         name='follow_category'),
]
