from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from annoying.utils import HttpResponseReload


@login_required
def tokens(request):
    """ View to return the buy tokens page """

    return render(request, 'tokens/tokens.html')


@login_required
def token_checkout(request):
    """ View to return the token checkout page """

    return render(request, 'tokens/token_checkout.html')


@login_required
def send_reward(request, receiver):
    sender = get_object_or_404(User, id=request.user.id)
    receiver = get_object_or_404(User, username=receiver)
    tokens = int(request.POST.get('reward'))

    if sender.userprofile.tokens_balance >= tokens:
        sender.userprofile.tokens_balance -= tokens
        receiver.userprofile.tokens_balance += tokens
        receiver.userprofile.tokens_score += tokens
        sender.userprofile.save()
        receiver.userprofile.save()
        messages.success(request, f'You sent {tokens} tokens to"{receiver}"')
    else:
        messages.success(request, 'Failed to send reward, insufficent balance')

    return HttpResponseReload(request)
