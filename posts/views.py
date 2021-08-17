from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .forms import AddPostForm, EditPostForm


class PostView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/add_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit_post.html'


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect(reverse('posts'))
