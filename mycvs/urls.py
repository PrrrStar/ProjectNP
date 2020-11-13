from django.urls import path
from .views import *

urlpatterns = [
    path('', mymap, name='mymap'),
]