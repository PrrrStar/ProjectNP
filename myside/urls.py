from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'myside'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('<category_slug>/', product_in_category, name='product_in_category'),

    path('api/index', ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetail.as_view())   
]

urlpatterns = format_suffix_patterns(urlpatterns)