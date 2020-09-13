from django.urls import path, include
from .views import *


urlpatterns = [
   path('', index, name='index'),
   path('products/<int:id>/', product_detail, name='product_detail'),
   path('<category_slug>/', product_in_category, name='product_in_category'),


    path('api/', ApiRoot.as_view(), name=ApiRoot.name),
    path('api/product-categories/', ProductCategoryList.as_view(), name=ProductCategoryList.name),
    path('api/product-categories/<int:pk>/', ProductCategoryDetail.as_view(), name=ProductCategoryDetail.name),
    path('api/products/', ProductList.as_view(), name=ProductList.name),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name=ProductDetail.name),
]
