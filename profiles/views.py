from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from posts.models import Post


def user_profile(request, user):
    author = get_object_or_404(User, username=user)
    user_posts = Post.objects.filter(author=author)
    user_posts = user_posts.order_by('-post_date')

    user_followed = False
    if author.userprofile.followers.filter(id=request.user.id).exists():
        user_followed = True

    context = {
        'author': author,
        'user_posts': user_posts,
        'user_followed': user_followed,
    }

    return render(request, 'profiles/user_profile.html', context)


@login_required
def follow_user(request, username):
    check_user = get_object_or_404(User, username=request.POST.get('username'))
    user_followed = False

    if request.user.username != username:
        if check_user.userprofile.followers.filter(
                                id=request.user.id).exists():
            check_user.userprofile.followers.remove(request.user)
            user_followed = False
        else:
            check_user.userprofile.followers.add(request.user)
            user_followed = True
            messages.success(request, f'You are now following "{username}"')
    else:
        messages.success(request, 'You can not follow your own profile.')

    if request.GET:
        if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])

    return HttpResponseRedirect(reverse('user_profile', args=[str(username)]))
