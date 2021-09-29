import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import OrderForm
from django.contrib import messages
from annoying.utils import HttpResponseReload


@login_required
def checkout(request, pk):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        form_data = {
            'card_name': request.POST['card_name'],
            'username': request.user.username,
            'email': request.POST['email'],
            'tokens': product.tokens,
            'order_total': product.display_price,
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            return redirect(reverse('checkout_success', args=[order]))
        else:
            messages.error(request, 'There was an error with your form, \
                please check the form and try again')

    else:
        total_price = product.price
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=total_price,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'username': request.user.username,
                'tokens': product.tokens,
            }
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


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order complete, {order.tokens} tokens \
        have been added to your account')

    context = {
        'order': order,
    }
    return render(request, 'tokens/success.html', context)


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
