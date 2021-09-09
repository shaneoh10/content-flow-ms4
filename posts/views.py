from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Category
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .forms import AddPostForm, EditPostForm, AddCommentForm, AddCategoryForm


class PostView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        context = super(PostView, self).get_context_data(*args, **kwargs)

        if self.request.GET:
            if 'q' in self.request.GET:
                query = self.request.GET['q']
                context['query'] = query

        return context

    def get_queryset(self):
        object_list = self.model.objects.all()
        if self.request.GET:
            if 'q' in self.request.GET:
                query = self.request.GET['q']
                queries = (
                           Q(title__icontains=query) |
                           Q(body__icontains=query) |
                           Q(category__category_name__icontains=query) |
                           Q(author__username__icontains=query)
                           )
                object_list = object_list.filter(queries)

            if 'sort' in self.request.GET:
                sortkey = self.request.GET['sort']
                sortkey = f'-{sortkey}'
                object_list = object_list.order_by(sortkey)

            return object_list
        else:
            return object_list.order_by('-post_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.like_count

        context['total_likes'] = total_likes
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'posts/add_category.html'

    def get_success_url(self):
        return reverse_lazy('posts')


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit_post.html'

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


def category_view(request, cat):
    posts_in_category = Post.objects.filter(category__category_name=cat)
    category = get_object_or_404(Category, category_name=cat)
    posts_in_category = posts_in_category.order_by('-post_date')

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sortkey = f'-{sortkey}'
        posts_in_category = posts_in_category.order_by(sortkey)

    return render(request, 'posts/categories.html',
                  {'posts_in_category': posts_in_category, 'cat': cat,
                   'category': category})


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


@login_required
def like_comment_view(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    post_id = comment.post.pk
    return HttpResponseRedirect(reverse('post_detail', args=[str(post_id)]))


@login_required
def follow_category(request, cat):
    category = get_object_or_404(Category, category_name=request.POST.get(
                                 'category_name'))
    if category.followers.filter(id=request.user.id).exists():
        category.followers.remove(request.user)
    else:
        category.followers.add(request.user)

    return HttpResponseRedirect(reverse('category', args=[str(cat)]))
