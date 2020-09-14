from django.contrib.auth.models import UserManager as DefaultUserManager
from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    img = models.ImageField(upload_to="comments/%Y/%m/%d",
                            blank=True, verbose_name="프로필사진")
    birth = models.DateField(verbose_name='생일')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'account_profile'
        app_label = 'account'  # <- account 앱 카테고리에서 관리되도록 한다.
