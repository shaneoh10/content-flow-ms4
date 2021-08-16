from django.shortcuts import render


def posts(request):
    """ View to return the posts page """

    return render(request, 'posts/posts.html')
