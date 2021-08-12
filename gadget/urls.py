from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_product, name='view_product'),
    path('', views.view_category, name='view_category'),
    path('product_detail/<product_id>',
         views.product_detail, name='product_detail'),

]
