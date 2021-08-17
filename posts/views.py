from django.shortcuts import render
from .models import Post


def posts(request):
    """ View to return the posts page """
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts
    }

    return render(request, 'posts/posts.html', context)
