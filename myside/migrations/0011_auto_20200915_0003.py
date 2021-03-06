# Generated by Django 3.1.1 on 2020-09-14 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myside', '0010_delete_recomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-created_at'], 'verbose_name': 'reply', 'verbose_name_plural': 'replies'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='updated_at',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='updated_at',
            new_name='modified_at',
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='myside.comment'),
        ),
    ]
