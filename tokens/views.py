from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product
from django.contrib import messages
from annoying.utils import HttpResponseReload


@login_required
def tokens(request):
    """ View to return the buy tokens page """
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'tokens/tokens.html', context)


@login_required
def token_checkout(request):
    """ View to return the token checkout page """

    context = {
        'stripe_public_key': 'pk_test_51JBGU9I5Jb6HSSk6B8EgzY9SVw1Ne9GCeHEzWgkG7riLah0QQ9pRV02hX0UAeB8Rx7oxknslUip8iXY5t4SVrCqG00pnJraVuQ',
        'client_secret': 'testing client secret',
    }
    return render(request, 'tokens/checkout.html', context)


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
