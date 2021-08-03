from django.shortcuts import render
from .forms import CategoryForm


def view_gadget(request):
    context = {}
    return render(request, 'gadget_view.html', context)


def add_category(request):
    form = CategoryForm()
    context = {'form': form}
    return render(request, 'add_category.html', context)
