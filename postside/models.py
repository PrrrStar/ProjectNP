from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=90, verbose_name='제목')
    img_url = models.URLField(max_length=200, verbose_name='이미지주소', blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    hits =models.IntegerField(default=0) 
    user_id = models.ForeignKey(
        "user.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'


class Post_recomment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    user_id = models.ForeignKey(
        "user.User", on_delete=models.CASCADE)
    post_id=models.ForeignKey("Post", on_delete=models.CASCADE)


    class Meta:
        db_table = 'post_recomment'
        verbose_name = '게시글 추천'
        verbose_name_plural = '게시글 추천'
    

class Post_comment(models.Model):
    img_url=models.URLField(max_length=200, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    user_id = models.ForeignKey(
        "user.User", on_delete=models.CASCADE)
    post_id=models.ForeignKey("Post", on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'post_comment'
        verbose_name = '게시글 코멘트'
        verbose_name_plural = '게시글 코멘트'
        

class Like_post_comment(models.Model):
    post_comment_id=models.ForeignKey("Post_comment", on_delete=models.CASCADE)
    good=models.IntegerField(verbose_name="좋아요", default=0)
    bad=models.IntegerField(verbose_name="싫어요", default=0)


class Like_post_recomment(models.Model):
    post_recomment_id=models.ForeignKey("Post_recomment", on_delete=models.CASCADE)
    good=models.IntegerField(verbose_name="좋아요", default=0)
    bad=models.IntegerField(verbose_name="싫어요", default=0)