import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .models import Product
from django.contrib import messages
from annoying.utils import HttpResponseReload

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSession(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = "https://8000-purple-porcupine-wogwv1tz.ws-eu16.gitpod.io"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            'images': [product.icon_url]
                        },
                    },
                    'quantity': 1,
                },
            ],
            payment_method_types=[
              'card',
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/tokens/success',
            cancel_url=YOUR_DOMAIN + '/tokens/cancel',
        )
        return redirect(checkout_session.url, code=303)


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
