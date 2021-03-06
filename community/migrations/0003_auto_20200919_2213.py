# Generated by Django 3.1.1 on 2020-09-19 13:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_auto_20200916_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': '게시글', 'verbose_name_plural': '게시글'},
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='authored', to='accounts.user', verbose_name='글쓴이'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]
