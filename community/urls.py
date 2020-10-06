from django.urls import path
from .views import *

urlpatterns = [
    path('<int:post_pk>/', post_detail, name="post_detail"),
    path('list/', post_list, name="post_list"),
    path('creation/', post_create, name="post_create"),
    path('<int:post_pk>/delete/', post_delete, name="post_delete"),
    path('<int:post_pk>/recommend/', post_recommend, name="post_recommend"),
    path('<int:post_pk>/derecommend/', post_derecommend, name="post_derecommend"),
    path('<int:post_pk>/comment/', comment_create, name="comment_create"),
    path('<int:post_pk>/comment/<int:comment_pk>/delete', post_comment_delete, name="post_comment_delete"),
    
    path('api/posts-list', PostList.as_view(), name=PostList.name),
    path('api/posts/<int:id>/', PostDetail.as_view(), name=PostDetail.name),
    path('api/comments/', CommentList.as_view(),name=CommentList.name),
]
