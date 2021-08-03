from django.shortcuts import render
from .forms import CategoryForm


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
