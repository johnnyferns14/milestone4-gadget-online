from django.db import models
from gadget.models import Product
from useraccount.models import UserAccount


class ProductReview(models.Model):
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=255, null=False, blank=False)
    review_body = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_title
