# Generated by Django 3.1.1 on 2020-09-20 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]