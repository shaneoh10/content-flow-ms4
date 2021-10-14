import stripe
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from .models import Product, Order, Withdrawal
from .forms import OrderForm, WithdrawalForm
from django.contrib import messages
from annoying.utils import HttpResponseReload


@login_required
def checkout(request, pk):
    """
    Displays checkout page and creates payment intent for stripe.
    Adds new order to database and stripe processes payment.
    """
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


@login_required
def checkout_success(request, order_number):
    """
    Displays order details if user checkout was successful.
    Sends email to user with order details.
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order complete, {order.tokens} tokens \
        have been added to your account')

    message = get_template("tokens/checkout_email.html").render({
        'order': order
    })

    mail = EmailMessage(
        "Content Flow Order confirmation",
        message,
        'contentflow@contentflow.com',
        [order.email],
    )
    mail.content_subtype = 'html'
    mail.send()

    context = {
        'order': order,
    }
    return render(request, 'tokens/success.html', context)


@login_required
def withdrawal(request):
    """
    Display token withdrawal page and creates new withdrawal
    in database when user submits withdrawal form
    """

    if request.method == 'POST':
        form_data = {
            'account_name': request.POST['account_name'],
            'iban': request.POST['iban'],
            'username': request.user.username,
            'email': request.POST['email'],
            'tokens': request.POST['tokens'],
            'withdrawal_total': float(request.POST['withdrawal_total']),
        }
        withdrawal_form = WithdrawalForm(form_data)
        user_profile = request.user.userprofile

        if withdrawal_form.is_valid():
            withdrawal = withdrawal_form.save(commit=False)
            withdrawal.save()
            user_profile.tokens_balance -= int(request.POST['tokens'])
            user_profile.save()
            return redirect(reverse('withdrawal_success', args=[withdrawal]))
        else:
            messages.error(request, 'There was an error with your form, \
                please check the form and try again')

    return render(request, 'tokens/withdrawal.html')


@login_required
def withdrawal_success(request, order_number):
    """
    Displays withdrawal details if user withdrawal was successful.
    Sends email to user with withdrawal details.
    """
    withdrawal = get_object_or_404(Withdrawal, order_number=order_number)
    messages.success(request, 'Withdrawal complete, the money should arrive \
        in the account provided within 3 business days.')

    message = get_template("tokens/withdrawal_email.html").render({
        'withdrawal': withdrawal
    })

    mail = EmailMessage(
        "Content Flow Withdrawal confirmation",
        message,
        'contentflow@contentflow.com',
        [withdrawal.email],
    )
    mail.content_subtype = 'html'
    mail.send()

    context = {
        'withdrawal': withdrawal,
    }
    return render(request, 'tokens/withdrawal_success.html', context)


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
