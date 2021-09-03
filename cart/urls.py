from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add/<product_id>/', views.add_cart, name="add_cart"),
    path('edit/<product_id>/', views.edit_cart, name="edit_cart"),
    path('subtract/<product_id>/', views.subtract_from_cart, name="subtract_from_cart"),
]
