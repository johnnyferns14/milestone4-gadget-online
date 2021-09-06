from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required

from useraccount.models import UserAccount
from django.contrib import messages
from .models import ProductReview
from gadget.models import Product
from .forms import ProductReviewForm


def view_review(request, product_id):
    """This view renders the list of reviews for a particular product"""
    product = get_object_or_404(Product, asin=product_id)
    reviews = ProductReview.objects.filter(product=product_id)
    context = {
        'product': product,
        'reviews': reviews,
        'product_id': product_id
    }
    return render(request, 'gadget/product_detail.html', context)


def add_review(request, product_id):
    """
    Here is the add review function which handles the way reviews are added
    """
    if request.user.is_authenticated:
        product = Product.objects.get(asin=product_id)
        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.review_title = request.POST['review_title']
                form.review_body = request.POST['review_body']
                form.author = UserAccount.objects.get(user=request.user)
                form.product = product
                form.save()
                messages.success(request, 'You successfully added the review!')
                return redirect('product_detail', product_id)
        else:
            form = ProductReviewForm()
        return redirect(reverse('product_detail', product_id))
    else:
        messages.error(request, 'You need to be logged in to review.')
        return redirect('home')

    context = {
        'form': form,
        'product': product,
        'product_id': product_id
    }
    return render(request, 'reviews/add_review.html', context)


@login_required
def edit_review(request, product_id, review_id):
    """
    Here is the edit review function which handles the editing of reviews
    """
    if request.user.is_authenticated:
        product = Product.objects.get(asin=product_id)
        review = ProductReview.objects.get(product=product, pk=review_id)

        if request.user.userprofile == review.author:
            if request.method == 'POST':
                form = ProductReviewForm(request.POST, instance=review)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.save()
                    messages.success(request,
                                     'Your review was successfully edited!')
                    return redirect('product_detail', product_id)
            else:
                form = ProductReviewForm(instance=review)
                context = {
                    'form': form
                }
            return render(request, 'reviews/edit_review.html', context)
        else:
            messages.error(request, 'You can only edit your own reviews.')
            return redirect('product_detail', product_id)
    else:
        return redirect('home')


@login_required
def delete_review(request, product_id, review_id):
    """
   The delete review function handles the way reviews are deleted
    """
    if request.user.is_authenticated:
        product = Product.objects.get (pk=product_id)
        review = ProductReview.objects.get(product=product, pk=review_id)

        if request.user.is_superuser:
            review.delete()
            messages.success(request, 'Your review was successfully deleted.')

        return redirect('product_detail', product_id)
    else:
        return redirect('home')
