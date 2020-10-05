from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', post_detail, name="post_detail"),
    path('list/', post_list, name="post_list"),
    path('creation/', post_create, name="post_create"),
    path('<int:pk>/recommend/', post_recommend, name="post_recommend"),
    path('<int:pk>/derecommend/', post_derecommend, name="post_derecommend"),
    path('<int:pk>/comment/', comment_create, name="comment_create"),
    #path('<int:pk>/derecommend', post_derecommend),
]
