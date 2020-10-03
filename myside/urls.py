from django.urls import path, include
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',happyChusok, name='happyChusok' ),
    path('index/', index, name='index'),
    path('category/<category_slug>/', product_in_category, name='product_in_category'),
    path('products/<slug>/', product_detail, name='product_detail'),
    
    path('products/<slug>/comments/', product_comment_create, name='product_comment_create'),
    path('products/<slug>/comments/<int:id>',product_comment_delete, name='product_comment_delete'),
    path('products/<slug>/comments/<int:id>/',product_comment_update, name='product_comment_update'),



    path('api/', ApiRoot.as_view(), name=ApiRoot.name),

    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/registration/', include('rest_auth.registration.urls')),

    path('api/products/', ProductList.as_view(), name=ProductList.name),
    path('api/product-categories/', ProductCategoryList.as_view(), name=ProductCategoryList.name),
    path('api/products/<slug>/', ProductDetail.as_view(), name=ProductDetail.name),
    path('api/products/<slug>/like', ProductLikeAPIToggle.as_view(), name=ProductLikeAPIToggle.name),

    path('api/comments/', CommentList.as_view(),name=CommentList.name),
    path('api/comments/<int:pk>/', CommentDetail.as_view(),name=CommentDetail.name),
    path('api/comments/<int:pk>/like', CommentLikeAPIToggle.as_view(), name=CommentLikeAPIToggle.name),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
