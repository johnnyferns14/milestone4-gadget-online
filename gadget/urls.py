from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_gadget, name='view_gadget'),
    path('add_category/', views.add_category, name='add_category'),
]
