from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<product_id>', views.add_review, name='add_review'),
    path('edit_review/<product_id>/<review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<product_id>/<review_id>/', views.delete_review, name='delete_review'),
]
