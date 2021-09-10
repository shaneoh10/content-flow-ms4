from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from posts.models import Post


def user_profile(request, user):
    user = get_object_or_404(User, username=user)
    user_posts = Post.objects.filter(author=user)

    context = {
        'user': user,
        'user_posts': user_posts
    }

    return render(request, 'profiles/user_profile.html', context)