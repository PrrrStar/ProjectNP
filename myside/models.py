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


class Category(MPTTModel):

    name    = models.CharField(max_length=20, verbose_name='카테고리', unique=True, db_index=True)
    parent  = TreeForeignKey('self', null=True, blank=True, verbose_name='상위 카테고리',related_name='children', on_delete=models.CASCADE)
    slug    = models.SlugField(max_length=20, db_index=True, allow_unicode=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together     = (('parent', 'slug',))
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
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


from mycvs.models import CVS
class Brand(models.Model):
    name        = models.CharField(max_length=20, verbose_name='브랜드', db_index=True)
    slug        = models.SlugField(max_length=20, db_index=True, allow_unicode=True)
    img         = models.ImageField(upload_to="brand", blank=True, null=True)
    
    cvs_name    = models.ForeignKey(CVS, verbose_name="지점명", null=True, blank=True,on_delete=models.CASCADE, related_name='cvs_name')


    class Meta:
        ordering            = ['-name']
        index_together      = [['id', 'slug']]
        verbose_name        = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name


class Product(models.Model):
    name                = models.CharField(max_length=20, db_index=True, verbose_name='제품명')
    img                 = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, null=True)
    description         = models.TextField(verbose_name='설명', blank=True)
    price               = models.DecimalField(verbose_name='가격', max_digits=10, decimal_places=0)
    stock               = models.PositiveIntegerField(verbose_name='재고')
    available_display   = models.BooleanField('판매 가능?', default=True)
    slug                = models.SlugField(max_length=20, db_index=True, allow_unicode=True)
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at         = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    
    category            = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    brand               = models.ManyToManyField(Brand, related_name='product_brand')
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

    def get_like_url(self):
        return reverse('product_like-toggle', kwargs={'slug': self.slug})

    def get_api_like_url(self):
        return reverse('product_like-api-toggle', kwargs={'pk': self.pk})


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
