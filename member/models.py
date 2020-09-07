from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'account_profile'
        app_label = 'account'  # <- account 앱 카테고리에서 관리되도록 한다.
