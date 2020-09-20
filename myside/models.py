from django.db import models
from django.urls import reverse
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):

    name    = models.CharField(max_length=20, verbose_name='카테고리', unique=True, db_index=True)
    parent  = TreeForeignKey('self', null=True, blank= True, verbose_name='상위 카테고리',related_name='children', on_delete=models.CASCADE)
    slug    = models.SlugField(max_length=20, db_index = True, allow_unicode=True)

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

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_in_category', args=[self.slug])
    
    def get_search_category_url(self):
        return reverse('search_product', kwargs={'category_id':self.id})


class Brand(models.Model):
    name    = models.CharField(max_length=20, verbose_name='브랜드', db_index=True)
    slug    = models.SlugField(max_length= 20, db_index=True, allow_unicode=True)
    img     = models.ImageField(upload_to="brand", blank=True, null=True)

    class Meta:
        ordering = ['-name']
        index_together = [['id','slug']]
        verbose_name        = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name        = models.CharField(max_length=32, verbose_name='태그명')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table            = "product_tag"
        verbose_name        = "Tag"
        verbose_name_plural = "Tags"


class Product(models.Model):
    name                = models.CharField(max_length = 20, db_index=True, verbose_name='제품명')
    category            = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'products')
    brand               = models.ManyToManyField(Brand)
    img                 = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, null=True)
    description         = models.TextField(verbose_name='설명', blank=True)
    price               = models.DecimalField(verbose_name='가격', max_digits = 10, decimal_places=0)
    stock               = models.PositiveIntegerField(verbose_name='재고')
    like                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='product_likes')
    available_display   = models.BooleanField('판매 가능?', default= True) 
    slug                = models.SlugField(max_length = 20, db_index=True, allow_unicode=True)
    tag                 = models.ManyToManyField(Tag)
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at         = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

    @property
    def image_url(self):
        if self.img:
            return self.img.url
        return '#'

    class Meta:
        ordering = ['-created_at','-modified_at']
        index_together = [['id','slug']]
        verbose_name        = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])

    def get_like_url(self):
        return reverse('product_like-toggle', kwargs={'id':self.id})

    def get_api_like_url(self):
        return reverse('product_like-api-toggle', kwargs={'pk':self.pk})

    

class Comment(models.Model):
    product     = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.CASCADE, related_name='comments')
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True, related_name='comments')
    img         = models.ImageField(upload_to="comments/%Y/%m/%d", blank=True)
    content     = models.TextField(max_length = 100, verbose_name='내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'comment'
        verbose_name_plural = 'comments'

class Reply(models.Model):
    comment     = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name='replies')
    #user       =
    content     = models.TextField(max_length=100, verbose_name='reply')
    created_at  = models.DateTimeField(auto_now_add= True, verbose_name='등록일')
    modified_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'reply'
        verbose_name_plural = 'replies'

    def __str__(self):
        return self.content

