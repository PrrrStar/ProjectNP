from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', post_detail),
    path('list/', post_list),
    path('write/', post_write),
]
