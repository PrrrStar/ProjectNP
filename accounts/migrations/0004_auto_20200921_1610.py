# Generated by Django 3.1.1 on 2020-09-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200918_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]