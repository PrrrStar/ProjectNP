# Generated by Django 3.1.1 on 2020-09-25 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0018_post_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='recommend_count',
        ),
        migrations.AddField(
            model_name='post',
            name='recommend',
            field=models.ManyToManyField(blank=True, related_name='recommends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Recommend',
        ),
    ]
