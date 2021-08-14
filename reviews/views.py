from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ProductReview
from gadget.models import Product
from .forms import ProductReviewForm


def view_review(request, product_id):
    product = get_object_or_404(Product, asin=product_id)
    reviews = ProductReview.objects.filter(product=product_id)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'view_review.html', context)


def add_review(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(asin=product_id)
        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.review_title = request.POST['review_title']
                form.review_body = request.POST['review_body']
                form.author = User.objects.get(user=request.user)
                form.product = product
                form.save()
                messages.success(request, 'You successfully added review!')
                return redirect('product_detail', product_id)
        else:
            form = ProductReviewForm()
        return redirect(reverse('product_detail', args=(product_id,)))
    else:
        messages.error(request, 'You need to be logged in to review.')
        return redirect('home')

    context = {
        'form': form,
        'product': product,
        'product_id': product_id
    }
    return render(request, 'add_review.html', context)
