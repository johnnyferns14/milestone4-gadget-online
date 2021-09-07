from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product
from reviews.forms import ProductReviewForm
from reviews.models import ProductReview


def view_category(request):
    """This view returns a list of categories"""
    categories = Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request, 'gadget/category_view.html', context)


def view_product(request):
    """This view renders the product template"""
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                return redirect(reverse('viewProduct'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'gadget/product_view.html', context)


def product_detail(request, product_id):
    """This view renders the details of the product"""
    is_favourite = False
    product = get_object_or_404(Product, asin=product_id)
    form = ProductReviewForm()
    reviews = ProductReview.objects.filter(product=product_id)

    if product.wished_for.filter(id=request.user.id).exists():
        is_favourite = True

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'is_favourite': is_favourite

    }
    return render(request, 'gadget/product_detail.html', context)
