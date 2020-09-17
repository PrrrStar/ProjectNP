from django.urls import path, include
from .views import *

from django.conf import settings

urlpatterns = [
    path('user_signup/', user_signup, name='user_signup'),
    path('user_login/', user_login, name='user_login'), 
    path('user_logout/', user_logout, name='user_logout'), 
]