from django.urls import path
from .views import *

urlpatterns = [
    path('', mymap, name='mymap'),
    path('add_mycvs/',add_mycvs, name="add_mycvs"),
]