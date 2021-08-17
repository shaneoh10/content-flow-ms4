from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import AddPostForm


class PostView(ListView):
    model = Post
    template_name = 'posts/posts.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/add_post.html'
