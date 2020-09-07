from django.urls import path, include
from .views import *

app_name = 'myside'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', product_detail, name='product_detail'),
    path('category/<category_slug>/', product_in_category, name='product_in_category'),
]
