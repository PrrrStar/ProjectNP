from django.urls import path, include
from .views import *

from django.conf import settings

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'), 
    path('logout/', logout, name='logout'), 
     
]