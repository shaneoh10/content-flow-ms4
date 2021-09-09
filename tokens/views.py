from django.shortcuts import render


def tokens(request):
    """ View to return the buy tokens page """

    return render(request, 'tokens/tokens.html')
