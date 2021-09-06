from .models import Category, Product


def category_navbar(request):
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
    }

    return context
