from django.urls import path, include
from .views import *

app_name = 'myside'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('<category_slug>/', product_in_category, name='product_in_category'),
]
