from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from gadget.models import Category, Product
from .forms import CategoryForm, ProductForm, UserAccountForm
from .models import UserAccount
from checkout.models import Order


def profile(request):
    profile = get_object_or_404(UserAccount, user=request.user)
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserAccountForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def add_category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
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
