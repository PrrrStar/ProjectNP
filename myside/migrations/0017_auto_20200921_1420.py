# Generated by Django 3.1.1 on 2020-09-21 05:20

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('myside', '0016_auto_20200921_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=20, verbose_name='slug'),
        ),
        migrations.CreateModel(
            name='TaggedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myside.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taggedProduct', to='myside.producttag')),
            ],
            options={
                'verbose_name': 'tagged product',
                'verbose_name_plural': 'tagged products',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='myside.TaggedProduct', to='myside.ProductTag', verbose_name='tags'),
        ),
    ]