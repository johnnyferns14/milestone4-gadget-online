from django.urls import path
from . import views

urlpatterns = [
    # path('', views.view_gadget, name='view_gadget'),
    path('', views.view_category, name='view_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('update_category/<category_id>', views.update_category, name='update_category'),
    path('delete_category/<category_id>', views.delete_category, name='delete_category'),
]
