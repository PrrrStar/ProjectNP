from django.urls import path, include
from .views import *

app_name = 'myside'

urlpatterns = [
    path('', index, name='index'),
]
