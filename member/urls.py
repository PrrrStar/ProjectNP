from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:id>/', profile_detail, name='profile_detail'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
]
