from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewCart, name="view_cart"),
    path('add/<product_id>/', views.addToCart, name="add_cart"),
]
