from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', post_detail, name="post_detail"),
    path('list/', post_list, name="post_list"),
    path('write/', post_write, name="post_write"),
    path('<int:pk>/recommend/', post_recommend, name="post_recommend"),
    path('<int:pk>/comment/', comment_write, name="comment_write"),
    #path('<int:pk>/derecommend', post_derecommend),
]
