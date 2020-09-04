from django.db import models
from django.urls import reverse

from mptt.models import MTPPModel, TreeForeignKey

# Create your models here.

class Category(models.Model):
    name    = models.CharField(max_length=20, verbose_name='상위 카테고리')
    parent  = TreeForeignKey('self', null=True, blank= True, related_name='children', db_index=True)
    slug    = models.SlugField(max_length=20, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name        = 'category'
        verbose_name_plural = 'categories'
        
    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self = True)
        except:
            ancestors= []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    class __str__(self):
        return self.first

class Brand(models.Model):
    name    = models.CharField(max_length=20, verbose_name='브랜드')
    img     = models.ImageField(upload_to="brand/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'brand'
        verbose_name_plural = 'brands'

class Product(models.Model):
    category            = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'products')
    brand               = models.ManyToManyField(Brand, through='Product_has_brand')

    name                = models.CharField(max_length = 20, verbose_name='제품명')
    SlugField           = models.SlugField(max_length = 20, unique = True)
    img                 = models.ImageField(upload_to="product/%Y/%m/%d", blank=True)
    description         = models.TextField(verbose_name='설명')
    price               = models.IntegerField(verbose_name='가격')
    stock               = models.IntegerField(verbose_name='재고')
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at         = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    available_display   = models.BooleanField('판매 가능?', default= True) 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'product'
        verbose_name_plural = 'products'

class Product_has_brand(models.Model):
    product     = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.SET_NULL, null=True)
    brand       = models.ForeignKey(Brand, verbose_name="브랜드명", on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    product     = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.CASCADE)
    img         = models.ImageField(upload_to="comment/%Y/%m/%d", blank=True)
    content     = models.TextField(verbose_name='내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        verbose_name        = 'comment'
        verbose_name_plural = 'comments'


class Recomment(models.Model):
    comment     = models.ForeignKey(Comment, verbose_name="댓글", on_delete=models.CASCADE)
    content     = models.TextField(verbose_name='대댓글내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        verbose_name        = 'recomment'
        verbose_name_plural = 'recomments'
