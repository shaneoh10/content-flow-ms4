from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def tokens(request):
    """ View to return the buy tokens page """

    return render(request, 'tokens/tokens.html')


@login_required
def token_checkout(request):
    """ View to return the token checkout page """

    return render(request, 'tokens/token_checkout.html')
