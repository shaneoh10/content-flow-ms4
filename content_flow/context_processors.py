from posts.models import Category


def all_categories(request):
    categories = Category.objects.all()
    categories = categories.order_by('category_name')
    context = {
        'categories': categories
    }
    return context
