from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    BOARD_LISTS=(('자유게시판','자유게시판'),('레시피연구소','레시피연구소'))
    title               = models.CharField(max_length=50,verbose_name="제목")
    content             = RichTextUploadingField(verbose_name="내용")
    board               = models.CharField(max_length=25, choices=BOARD_LISTS,verbose_name="게시판")
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='authored', verbose_name='글쓴이', on_delete=models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at         = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    hits                = models.PositiveIntegerField(default=0, verbose_name='조회수')
    recommend_count     = models.PositiveIntegerField(default=0, verbose_name='추천')
    #derecommend_user   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='derecommend_posts', verbose_name='비추')
    
    def __str__(self):
        return self.title

    @property
    def update_hits(self):
        self.hits+=1
        self.save()
    
    @property
    def plus_recommend_count(self):
        self.recommend_count+=1
        self.save()
    
    @property
    def minus_recommend_count(self):
        self.recommend_count-=1
        self.save()
        
    
    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'post'
        verbose_name_plural = 'posts'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Recommend(models.Model):
    post        = models.ForeignKey(Post, verbose_name="글", on_delete=models.CASCADE, related_name='recommend')
    user        = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommend')
    class Meta:
        ordering            = ['-id']
        verbose_name        = 'recommend'
        verbose_name_plural = 'recommends'    


class Comment(models.Model):
    post        = models.ForeignKey(Post, verbose_name="글", on_delete=models.CASCADE, related_name='comment')
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment')
    content     = models.TextField(max_length = 100, verbose_name='내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at = models.DateTimeField(auto_now = True, verbose_name='수정날짜')

    class Meta:
        ordering            = ['-created_at']
        verbose_name        = 'comment'
        verbose_name_plural = 'comments'

