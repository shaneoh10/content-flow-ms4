from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostView(ListView):
    model = Post
    template_name = 'posts/posts.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
