from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView)
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .forms import AddPostForm, EditPostForm, AddCommentForm


class PostView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.like_count

        context['total_likes'] = total_likes
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/add_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit_post.html'

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


def category_view(request, cat):
    posts_in_category = Post.objects.filter(category__category_name=cat)
    return render(request, 'posts/categories.html',
                  {'posts_in_category': posts_in_category, 'cat': cat})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect(reverse('posts'))


@login_required
def like_post_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
