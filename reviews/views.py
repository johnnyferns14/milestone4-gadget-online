from django.shortcuts import render, get_object_or_404
from .models import ProductReview
from gadget.models import Product
from .forms import ProductReviewForm


def viewReview(request, product_id):
    product = get_object_or_404(Product, asins=product_id)
    reviews = ProductReview.objects.filter(product=product_id)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'view_review.html', context)


def addReview(request, product_id):
    product = get_object_or_404(Product, asins=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            product_review = form.save(commit=False)
            product_review.save()
    else:
        form = ProductReviewForm()
    return render(request, 'add_review.html', {'form': form})
