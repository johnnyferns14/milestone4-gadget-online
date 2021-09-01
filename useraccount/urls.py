from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_category/<category_id>',
         views.update_category, name='update_category'),
    path('update_product/<product_id>',
         views.update_product, name='update_product'),
    path('delete_category/<category_id>',
         views.delete_category, name='delete_category'),
    path('delete_product/<product_id>',
         views.delete_product, name='delete_product'),
]
