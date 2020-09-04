from django.db import models

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=90, verbose_name='제목')
    img         = models.ImageField(upload_to="post/%Y/%m/%d", blank=True)
    content     = models.TextField(verbose_name='내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    hits        = models.IntegerField(default=0) 

    def __str__(self):
        return self.title

    class Meta:
        db_table            = 'post'
        verbose_name        = '게시글'
        verbose_name_plural = '게시글'

class Post_comment(models.Model):
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)
    img         = models.ImageField(upload_to="post_comment/%Y/%m/%d", blank=True)
    content     = models.TextField(verbose_name='내용')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    
    class Meta:
        db_table            = 'post_comment'
        verbose_name        = '게시글 댓글'
        verbose_name_plural = '게시글 댓글'
        

class Post_recomment(models.Model):
    post_comment    = models.ForeignKey(Post_comment, on_delete=models.CASCADE)
    content         = models.TextField(verbose_name='내용')
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')


    class Meta:
        db_table            = 'post_recomment'
        verbose_name        = '게시글 대댓글'
        verbose_name_plural = '게시글 대댓글'
    

class Like_post_comment(models.Model):
    post_comment    = models.ForeignKey(Post_comment, on_delete=models.CASCADE)
    good            = models.IntegerField(verbose_name="좋아요", default=0)
    bad             = models.IntegerField(verbose_name="싫어요", default=0)


class Like_post_recomment(models.Model):
    post_recomment  = models.ForeignKey(Post_recomment, on_delete=models.CASCADE)
    good            = models.IntegerField(verbose_name="좋아요", default=0)
    bad             = models.IntegerField(verbose_name="싫어요", default=0)