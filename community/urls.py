from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', post_detail, name="detail"),
    path('list/', post_list, name="list"),
    path('write/', post_write, name="write"),
    path('<int:pk>/recommend', post_recommend, name="recommend"),
    #path('<int:pk>/derecommend', post_derecommend),
]
