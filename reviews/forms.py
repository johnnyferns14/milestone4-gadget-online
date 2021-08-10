from django.forms import ModelForm
from .models import ProductReview


class ProductReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review_title','review_body',]
