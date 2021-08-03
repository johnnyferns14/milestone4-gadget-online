from django.shortcuts import render
from .forms import CategoryForm
from .models import Category


def view_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories_view.html', context)


def view_gadget(request):
    context = {}
    return render(request, 'gadget_view.html', context)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
    context = {'form': form}
    return render(request, 'add_category.html', context)


def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        category.delete()
    context = {'category': category, 'category_id': category_id}
    return render(request, 'delete_category.html', context)
