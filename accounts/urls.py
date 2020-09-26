from django.urls import path, include
from .views import *

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('user_signup/', user_signup, name='user_signup'),
    path('user_login/', user_login, name='user_login'), 
    path('user_logout/', csrf_exempt(user_logout), name='user_logout'), 

    path('profile/', user_profile, name= 'user_profile'),
    path('myprofile/', edit_user_profile, name = 'edit_user_profile'),
    path('delete/', delete_user_profile, name='delete_user_profile'),
]