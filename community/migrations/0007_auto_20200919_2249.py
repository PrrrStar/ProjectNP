# Generated by Django 3.1.1 on 2020-09-19 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20200919_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommend',
            options={'ordering': ['-id'], 'verbose_name': 'recommend', 'verbose_name_plural': 'recommends'},
        ),
        migrations.RenameField(
            model_name='recommend',
            old_name='account',
            new_name='user',
        ),
    ]
