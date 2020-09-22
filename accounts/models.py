from django.db import models
from django.shortcuts import reverse

'''
이메일 (email)
이름 (username)

별명
프사
성별
생일
'''

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    GENDER_MALE     = "male"
    GENDER_FEMALE   = "female"
    GENDER_OTHER    = "other"

    GENDER_CHOICES=(
        (GENDER_MALE,"Male"),
        (GENDER_FEMALE,"Female"),
        (GENDER_OTHER,"Other"),
    )
    username        = None
    email           = models.EmailField(max_length=255, unique=True)
    nickname        = models.CharField(max_length=10, null=True, unique=True)
    profile         = models.ImageField(upload_to='profile', default="static/logo/person-24px.png", blank=True, null=True)
    introduction    = models.TextField(max_length=100, blank=True, null=True)
    gender          = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True)
    birth           = models.DateField(blank=True, null=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nickname',]
    
    def get_user_profile_url(self):
        return reverse('user_profile', kwargs={'id':self.id})
