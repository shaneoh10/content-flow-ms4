import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from profiles.models import UserProfile
from .models import Post, Comment, Category
from django.db.models import Q, Count
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from annoying.utils import HttpResponseReload
from .forms import AddPostForm, EditPostForm, AddCommentForm, AddCategoryForm


class PostView(ListView):
    """
    View to display all available posts, users have the
    ability to query the database and sort posts
    """
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
                object_list = object_list.order_by('-post_date')
                if len(query) < 1:
                    object_list = {}

            if 'sort' in self.request.GET:
                sortkey = self.request.GET['sort']
                if sortkey == 'likes':
                    object_list = object_list.annotate(
                        like_count=Count('likes')).order_by(
                            '-like_count', '-post_date')
            return object_list
        else:
            return object_list.order_by('-post_date')


class PostDetailView(DetailView):
    """ View to display individual posts """
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.like_count
        user_followers = current_post.author.userprofile.followers.count

        post_liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            post_liked = True

        user_followed = False
        if current_post.author.userprofile.followers.filter(
                            id=self.request.user.id).exists():
            user_followed = True

        comments = current_post.comments.all().order_by('-comment_date')

        context['user_followers'] = user_followers
        context['user_followed'] = user_followed
        context['post_liked'] = post_liked
        context['total_likes'] = total_likes
        context['comments'] = comments
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    """ Add a new post to the database """
    model = Post
    form_class = AddPostForm
    template_name = 'posts/add_post.html'

    def form_valid(self, form):
        messages.success(self.request,
                         f'New post added: "{form.instance.title}"')
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(LoginRequiredMixin, CreateView):
    """ Allows users to add a new category to the database """
    model = Category
    form_class = AddCategoryForm
    template_name = 'posts/add_category.html'

    def form_valid(self, form):
        messages.success(self.request,
                         f'New category added: "{form.instance.category_name}"'
                         )
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts')


class EditPostView(LoginRequiredMixin, UpdateView):
    """
    Allows users to edit their own posts or superuser
    to edit any post
    """
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit_post.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        user = self.request.user
        if user.id == post.author.id or user.is_superuser:
            messages.success(self.request,
                             f'Successfully edited post: \
                             "{form.instance.title}"')
            return super().form_valid(form)
        else:
            messages.error(self.request, "You can only edit your own posts")
            return HttpResponseReload(self.request)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


class AddCommentView(LoginRequiredMixin, CreateView):
    """ Allows users to add a comment to an individual post """
    model = Comment
    form_class = AddCommentForm
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        messages.success(self.request, 'Successfully added comment')
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


def category_view(request, cat):
    """
    Displays all posts in a chosen category,
    posts can be sorted by date or likes
    """
    posts_in_category = Post.objects.filter(category__category_name=cat)
    category = get_object_or_404(Category, category_name=cat)
    posts_in_category = posts_in_category.order_by('-post_date')

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey == 'likes':
                posts_in_category = posts_in_category.annotate(
                    like_count=Count('likes')).order_by(
                        '-like_count', '-post_date')

    category_followed = False
    if category.followers.filter(id=request.user.id).exists():
        category_followed = True

    context = {
        'category_followed': category_followed,
        'posts_in_category': posts_in_category,
        'cat': cat,
        'category': category,
        }
    return render(request, 'posts/categories.html', context)


@login_required
def custom_feed_view(request, exception):
    """
    Displays user's custom feed. Shows only posts in categories followed
    by current user and posts written by users followed by current user
    """
    users_followed = UserProfile.objects.filter(followers=request.user.id)
    categories_followed = Category.objects.filter(followers=request.user.id)

    cat_posts = []
    for category in categories_followed:
        if Post.objects.filter(category__category_name=category):
            cat_posts.append(Post.objects.filter(
                          category__category_name=category))

    user_posts = []
    for author in users_followed:
        if Post.objects.filter(author__userprofile=author.id):
            user_posts.append(Post.objects.filter(
                              author__userprofile=author.id))

    custom_feed = []
    for posts in cat_posts:
        for post in posts:
            if post not in custom_feed:
                custom_feed.append(post)

    for posts in user_posts:
        for post in posts:
            if post not in custom_feed:
                custom_feed.append(post)

    custom_feed.sort(key=lambda x: x.post_date, reverse=True)

    context = {
        'custom_feed': custom_feed
    }
    return render(request, 'posts/custom_feed.html', context)


@login_required
def delete_post(request, post_id):
    """
    View to delete posts, post can be deleted by the
    user who created it or a superuser
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user.id == post.author.id or request.user.is_superuser:
        if post.image:
            if 'USE_AWS' in os.environ:
                post.image.delete(save=False)
            else:
                os.remove(post.image.path)
        post.delete()
        messages.success(request, f'Successfully deleted post: "{post.title}"')
        return redirect(reverse('posts'))
    else:
        messages.error(request, 'You can only delete your own posts')
        return redirect(reverse('posts'))


@login_required
def delete_comment(request, comment_id):
    """
    View to delete comments, comments can be deleted by the
    user who wrote it or a superuser
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.id == comment.author.id or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Successfully deleted comment')
        return HttpResponseReload(request)
    else:
        messages.error(request, 'You can only delete your own comments')
        return HttpResponseReload(request)


@login_required
def like_post_view(request, pk):
    """ Allows users to like and unlike a post """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post_liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post_liked = False
    else:
        post.likes.add(request.user)
        post_liked = True

    return HttpResponseReload(request)


@login_required
def like_comment_view(request, pk):
    """ Allows users to like and unlike a comment """
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    post_id = comment.post.pk
    return HttpResponseRedirect(reverse('post_detail', args=[str(post_id)]))


@login_required
def follow_category(request, cat):
    """ Allows users to follow a category """
    category = get_object_or_404(Category, category_name=request.POST.get(
                                 'category_name'))
    category_followed = False
    if category.followers.filter(id=request.user.id).exists():
        category.followers.remove(request.user)
        category_followed = False
    else:
        category.followers.add(request.user)
        category_followed = True
        messages.success(request, f'You are now following "{cat}"')

    return HttpResponseRedirect(reverse('category', args=[str(cat)]))
