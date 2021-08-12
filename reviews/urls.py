from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_review, name='view_review'),
    path('add_review/<product_id>', views.add_review, name='add_review'),
]
