from django.urls import path, include
from .views import *

app_name = 'myside'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]
