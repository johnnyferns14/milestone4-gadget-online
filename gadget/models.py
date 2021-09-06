from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    asin = models.CharField(
        max_length=10, primary_key=True, null=False, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=50, null=True, blank=True)
    wished_for = models.ManyToManyField(User, related_name='favourites', blank=True)

    def __str__(self):
        return self.title
