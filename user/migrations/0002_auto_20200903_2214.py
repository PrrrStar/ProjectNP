# Generated by Django 3.1 on 2020-09-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=16, verbose_name='등급'),
        ),
    ]