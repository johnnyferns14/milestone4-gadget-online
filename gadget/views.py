from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product


def view_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request, 'category_view.html', context)


def view_product(request):
    products = Product.objects.all()
    context = {
        'products': products
        }
    return render(request, 'product_view.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, asin=product_id)

    context = {
        'product': product

    }
    return render(request, 'product_detail.html', context)
