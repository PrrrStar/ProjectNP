# Generated by Django 3.1.1 on 2020-10-04 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]