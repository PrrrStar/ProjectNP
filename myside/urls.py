from django.urls import path, include
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_product, name='search_product'),
    path('search/<int:category_id>', search_product, name='search_product'),
    path('category/<category_slug>/', product_in_category, name='product_in_category'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('products/<int:id>/comment/', comment_create, name='comment_create'),
    path('products/<int:id>/like',ProductLikeToggle.as_view(), name='product_like-toggle'),
    path('mymap/', mymap, name='mymap'),

    path('api/', ApiRoot.as_view(), name=ApiRoot.name),
    path('api/product-categories/', ProductCategoryList.as_view(), name=ProductCategoryList.name),
    path('api/product-categories/<int:pk>/', ProductCategoryDetail.as_view(), name=ProductCategoryDetail.name),
    path('api/products/', ProductList.as_view(), name=ProductList.name),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name=ProductDetail.name),
    path('api/products/<int:pk>/like', ProductLikeAPIToggle.as_view(), name=ProductLikeAPIToggle.name),
    path('api/comments/', CommentList.as_view(),name=CommentList.name),
    path('api/comments/<int:pk>/', CommentDetail.as_view(),name=CommentDetail.name),
    path('api/replies/', ReplyList.as_view(), name=ReplyList.name),
    path('api/replies/<int:pk>/', ReplyDetail.as_view(), name=ReplyDetail.name),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
