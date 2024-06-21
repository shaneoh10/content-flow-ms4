from django.shortcuts import render


def error_404(request, exception):
    return render(request, "auth/404.html")


def error_500(request):
    return render(request, "auth/500.html")
