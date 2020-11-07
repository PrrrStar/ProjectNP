from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase
# Create your models here.


class ProductTag(TagBase):
    slug    = models.SlugField(verbose_name='slug',max_length=20, allow_unicode=True)

    class Meta:
        index_together      = [['name', 'slug']]
        unique_together     = (('name', 'slug',))
        verbose_name        = 'tags'
        verbose_name_plural = 'tags'


class TaggedProduct(TaggedItemBase):
    content_object  = models.ForeignKey('Product', on_delete=models.CASCADE)
    tag             = models.ForeignKey('ProductTag', related_name='taggedProduct', on_delete=models.CASCADE)

    class Meta:
        verbose_name        = 'tagged product'
        verbose_name_plural = 'tagged products'


class Category(models.Model):
    first               =models.CharField(max_length=20, verbose_name='상위카테고리', null=True)
    second              =models.CharField(max_length=20, verbose_name='하위카테고리', null=True)
    slug                =models.SlugField(max_length=20, db_index=True, allow_unicode=True, null=True)
    class Meta:
        ordering            = ['-first', '-second']
        index_together      = [['id', 'slug']]
        verbose_name        = 'category'
        verbose_name_plural = 'cateogories'
    def __str__(self):
        return self.second
    def get_absolute_url(self):
        return reverse('product_in_category', args=[self.slug])

class Product(models.Model):
    name                = models.CharField(max_length=20, db_index=True, verbose_name='제품명')
    img                 = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, null=True)
    description         = models.TextField(verbose_name='설명', blank=True)
    price               = models.DecimalField(verbose_name='가격', max_digits=10, decimal_places=0)
    available_display   = models.BooleanField('판매 가능?', default=True)
    slug                = models.SlugField(max_length=20, db_index=True, allow_unicode=True)
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at         = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    category            = models.ForeignKey(Category, verbose_name='category',related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    like                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='product_likes')
    tags                = TaggableManager(verbose_name='tags',blank=True, through=TaggedProduct)

    @property
    def image_url(self):
        if self.img:
            return self.img.url
        return '#'

    class Meta:
        ordering            = ['-created_at', '-modified_at']
        index_together      = [['id', 'slug']]
        verbose_name        = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def get_api_like_url(self):
        return reverse('product_like-api-toggle', kwargs={'slug': self.slug})


class Comment(models.Model):
    img             = models.ImageField(upload_to="comments/%Y/%m/%d", blank=True, null=True)
    content         = models.TextField(max_length=100, verbose_name='내용')
    stars           = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    like            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='comment_likes')
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_at     = models.DateTimeField(auto_now=True)

    product         = models.ForeignKey(Product, verbose_name="제품명", on_delete=models.CASCADE, related_name='comments')
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True, related_name='comments_author')

    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'comment'
        verbose_name_plural = 'comments'

    def get_api_like_url(self):
        return reverse('comment_like-api-toggle', kwargs={'pk': self.pk})


class Reply(models.Model):
    comment         = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    # user       =
    content         = models.TextField(max_length=100, verbose_name='reply')
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'reply'
        verbose_name_plural = 'replies'

    def __str__(self):
        return self.content
