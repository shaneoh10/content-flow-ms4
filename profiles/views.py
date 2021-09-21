from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from annoying.utils import HttpResponseReload
from django.http import HttpResponseRedirect
from posts.models import Post
from .models import UserProfile
from .forms import EditProfileForm


def user_profile(request, user):
    author = get_object_or_404(User, username=user)
    user_posts = Post.objects.filter(author=author)
    user_posts = user_posts.order_by('-post_date')
    user_followers = author.userprofile.followers.count

    user_followed = False
    if author.userprofile.followers.filter(id=request.user.id).exists():
        user_followed = True

    context = {
        'author': author,
        'user_posts': user_posts,
        'user_followed': user_followed,
        'user_followers': user_followers,
    }

    return render(request, 'profiles/user_profile.html', context)


@login_required
def user_settings(request, username):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user__username=username)

    if request.user.username == username:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Update failed. Please ensure the \
                               form is valid.')
        else:
            form = EditProfileForm(instance=profile)
    else:
        messages.error(request,
                       'Prohibited. You can only edit your own profile')
        return redirect(reverse('posts'))

    context = {
        'form': form,
    }

    return render(request, 'profiles/user_settings.html', context)


@login_required
def delete_account(request, username):
    account = get_object_or_404(User, id=request.user.id)

    if account.username == username:
        account.delete()
        messages.success(request, 'Account deleted')
        return HttpResponseReload(request)
    else:
        messages.error(request, 'Error: You can only delete your own account')
        return HttpResponseReload(request)


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
