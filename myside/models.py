from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    first   = models.CharField(max_length=20, verbose_name='대주제')
    second  = models.CharField(max_length=20, verbose_name='소주제')

    class Meta:
        db_table            = 'category'
        verbose_name        = '카테고리'
        verbose_name_plural = '카테고리'

class Brand(models.Model):
    name    = models.CharField(max_length=20, verbose_name='브랜드')
    img     = models.ImageField(upload_to="brand/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table            = 'brand'
        verbose_name        = '브랜드'
        verbose_name_plural = '브랜드'

class Product(models.Model):
    category            = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name = 'products')
    brand               = models.ManyToManyField(Brand, through='Product_has_brand')

    name                = models.CharField(max_length=20, verbose_name='제품명')
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
        db_table            = 'product'
        verbose_name        = '제품'
        verbose_name_plural = '제품'

class Product_has_brand(models.Model):
    product     = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.SET_NULL, null=True)
    brand       = models.ForeignKey(Brand, verbose_name="브랜드명", on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    product     = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.CASCADE)
    img         = models.ImageField(upload_to="comment/%Y/%m/%d", blank=True)
    content     = models.TextField(verbose_name='내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table            = 'comment'
        verbose_name        = '댓글'
        verbose_name_plural = '댓글'


class Recomment(models.Model):
    comment     = models.ForeignKey(Comment, verbose_name="댓글", on_delete=models.CASCADE)
    content     = models.TextField(verbose_name='대댓글내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table            = 'recomment'
        verbose_name        = '대댓글'
        verbose_name_plural = '대댓글'


class Like_product(models.Model):
    product     = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.CASCADE)
    good        = models.IntegerField(verbose_name="좋아요", default=0)
    bad         = models.IntegerField(verbose_name="싫어요", default=0)


class Like_comment(models.Model):
    comment     = models.ForeignKey(Comment, on_delete=models.CASCADE)
    good        = models.IntegerField(verbose_name="좋아요", default=0)
    bad         = models.IntegerField(verbose_name="싫어요", default=0)


class Like_recomment(models.Model):
    recomment   = models.ForeignKey(Recomment, on_delete=models.CASCADE)
    good        = models.IntegerField(verbose_name="좋아요", default=0)
    bad         = models.IntegerField(verbose_name="싫어요", default=0)
        



    

