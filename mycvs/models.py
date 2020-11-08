from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class CVS(models.Model):
    name        = models.CharField(max_length=20, db_index=True, verbose_name='지점명')
    slug        = models.SlugField(max_length=20, verbose_name='지점명', db_index=True, allow_unicode=True, null=True)
    latitude    = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='위도')
    longitude   = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='경도')
    brand       = models.CharField(max_length=20, verbose_name='편의점 브랜드', null=True)
    brand_logo  = models.ImageField(upload_to="brand", blank=True, null=True)
    user        = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name='내 편', related_name='mycvs')

    class Meta:
        ordering            = ['-name']
        index_together      = [['id', 'slug']]
        verbose_name        = 'cvs'
        verbose_name_plural = 'cvs'


from myside.models import Product
class Stock(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    cvs     = models.ForeignKey(CVS, related_name='cvs', on_delete=models.CASCADE)
    stock   = models.PositiveIntegerField(default=0, verbose_name='재고')

    class Meta:
        verbose_name        = 'stock'
        verbose_name_plural = 'stocks'
