from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category


def view_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request, 'category_view.html', context)



def add_category(request): 
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
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


def view_gadget(request):
    context = {}
    return render(request, 'gadget_view.html', context)
