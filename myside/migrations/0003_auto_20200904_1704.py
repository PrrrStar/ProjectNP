# Generated by Django 3.1.1 on 2020-09-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myside', '0002_auto_20200904_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
    ]
