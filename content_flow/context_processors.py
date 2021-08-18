from posts.models import Category


def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context
