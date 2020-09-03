from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='이름')
    email = models.EmailField(verbose_name='이메일')
    nickname = models.CharField(max_length=20, verbose_name='별명')
    password = models.CharField(max_length=45, verbose_name='비밀번호')
    gender = models.CharField(max_length=16, verbose_name='성별',
                              choices=(
                                  ('male', 'male'),
                                  ('female', 'female')
                              ))
    birth = models.DateField(auto_now=False, auto_now_add=False)
    rank = models.CharField(max_length=8, verbose_name='등급',
                            choices=(
                                ('admin', 'admin'),
                                ('user', 'user')
                            ))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
