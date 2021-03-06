from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email           = models.EmailField(max_length=255, unique=True)
    username        = models.TextField(max_length=100, blank=True, null=True)
    nickname        = models.CharField(max_length=10, null=True, unique=True)
    profile         = models.ImageField(upload_to='profile', default="profile/default_profile.png", blank=True, null=True)
    introduction    = models.TextField(max_length=100, blank=True, null=True)
    birth           = models.DateField(blank=True, null=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nickname',]

    
    def __str__(self):
        return self.email