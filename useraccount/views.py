from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from gadget.models import Category, Product
from .forms import CategoryForm, ProductForm, UserAccountForm
from .models import UserAccount
from checkout.models import Order


def profile(request):
    """This view enables the user to update the save default save information"""
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

    template = 'useraccount/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)


def order_history(request, order_number):
    """This view gives details of previous orders of specific user"""
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
            messages.error(request, 'Sorry the category could not be added')
    else:
        form = CategoryForm()
    context = {'form': form}
    return render(request, 'useraccount/add_category.html', context)


def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(request, 'Category successfully updated.')
        return redirect('view_category')
    else:
        messages.error(request, 'Sorry, category updation unsuccessful.')
    context = {
        'category': category,
        'form': form
        }

    return render(request, 'useraccount/update_category.html', context)


def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully.')
    return redirect('view_category')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
        else:
            messages.error(request, 'Sorry, could not add the product')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'useraccount/add_product.html', context)


def update_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = Product.objects.get(asin=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updation success.')
            return redirect('view_product')
        else:
            messages.error(request, 'Sorry, product updation failed.')
    else:
        form = ProductForm(instance=product)
    context = {
        'product': product,
        'form': form
        }
    return render(request, 'useraccount/update_product.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(asin=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect('view_product')
