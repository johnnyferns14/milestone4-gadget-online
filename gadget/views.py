from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoryForm, ProductForm
from .models import Category, Product


def view_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request, 'category_view.html', context)


def add_category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            if not category:
                form.save()
                messages.success(request, 'Category added successfully.')
            else:
                messages.error(request, 'Category already exists')
                return redirect('view_category')
    else:
        form = CategoryForm()
    context = {'form': form}
    return render(request, 'add_category.html', context)


def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('view_category')
    context = {
        'category': category,
        'form': form
        }

    return render(request, 'update_category.html', context)


def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('view_category')


def view_product(request):
    products = Product.objects.all()
    context = {
        'products': products
        }
    return render(request, 'product_view.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'add_product.html', context)


def update_product(request, product_id):
    product = Product.objects.get(asin=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('view_product')
    context = {
        'product': product,
        'form': form
        }
    return render(request, 'update_product.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(asin=product_id)
    product.delete()
    return redirect('view_product')
