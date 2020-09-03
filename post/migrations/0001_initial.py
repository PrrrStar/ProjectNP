# Generated by Django 3.1.1 on 2020-09-03 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='제목')),
                ('img', models.ImageField(blank=True, upload_to='post/%Y/%m/%d')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('hits', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글',
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Post_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='post_comment/%Y/%m/%d')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
            options={
                'verbose_name': '게시글 댓글',
                'verbose_name_plural': '게시글 댓글',
                'db_table': 'post_comment',
            },
        ),
        migrations.CreateModel(
            name='Post_recomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post_comment')),
            ],
            options={
                'verbose_name': '게시글 대댓글',
                'verbose_name_plural': '게시글 대댓글',
                'db_table': 'post_recomment',
            },
        ),
        migrations.CreateModel(
            name='Like_post_recomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.IntegerField(default=0, verbose_name='좋아요')),
                ('bad', models.IntegerField(default=0, verbose_name='싫어요')),
                ('post_recomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post_recomment')),
            ],
        ),
        migrations.CreateModel(
            name='Like_post_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.IntegerField(default=0, verbose_name='좋아요')),
                ('bad', models.IntegerField(default=0, verbose_name='싫어요')),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post_comment')),
            ],
        ),
    ]
