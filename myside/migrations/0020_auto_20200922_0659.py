# Generated by Django 3.1.1 on 2020-09-21 21:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myside', '0019_remove_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='stars',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]