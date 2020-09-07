from rest_framework import serializers
from .model import *
from django.contrib.auth.models import User


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class 