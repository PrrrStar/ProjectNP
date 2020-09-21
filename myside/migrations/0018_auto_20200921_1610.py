# Generated by Django 3.1.1 on 2020-09-21 07:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myside', '0017_auto_20200921_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='producttag',
            index_together={('name', 'slug')},
        ),
    ]
