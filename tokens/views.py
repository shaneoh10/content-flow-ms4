import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product
from django.contrib import messages
from annoying.utils import HttpResponseReload


@login_required
def checkout(request, pk):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    product = get_object_or_404(Product, id=pk)
    total_price = product.price

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=total_price,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.error(request, 'Stripe public key not set.')

    context = {
        'product': product,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'total_price': total_price,
    }
    return render(request, 'tokens/checkout.html', context)


def order_success(request):
    return render(request, 'tokens/success.html')


def order_cancel(request):
    return render(request, 'tokens/cancel.html')


@login_required
def tokens(request):
    """ Displays the buy tokens page """
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'tokens/tokens.html', context)


@login_required
def send_reward(request, receiver):
    """
    Allows users to reward other users with tokens if
    they have a sufficient balance to do so
    """
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
