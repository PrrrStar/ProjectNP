# Generated by Django 3.1.1 on 2020-09-19 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20200919_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommend',
            old_name='user',
            new_name='account',
        ),
    ]
