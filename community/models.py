from django.db import models

# Create your models here.
class Post(models.Model):
    title           = models.CharField(max_length=50,verbose_name="제목")
    content         = models.TextField(verbose_name="내용")
    #author=models.ForeignKey()
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modified_at     = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    hits            = models.PositiveIntegerField(default=0, verbose_name='조회수')
    

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hits+=1
        self.save()
    class Meta:
        ordering = ['-id']
        verbose_name        = '게시글'
        verbose_name_plural = '게시글'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Like_post(models.Model):
    post        = models.ForeignKey(Post, verbose_name="게시글", on_delete=models.CASCADE,  related_name='likes')
    good        = models.IntegerField(verbose_name="좋아요", default=0)
    bad         = models.IntegerField(verbose_name="싫어요", default=0)

