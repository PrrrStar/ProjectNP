from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class CVS(models.Model):
    name        = models.CharField(max_length=20, db_index=True, verbose_name='제품명')
    latitude    = models.DecimalField(max_digits=9, decimal_places=6)
    longitude   = models.DecimalField(max_digits=9, decimal_places=6)
    
    mycvs       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='mycvs')