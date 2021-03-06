# Generated by Django 2.1.5 on 2019-01-21 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190121_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.SubCategory', verbose_name='Подкатегория'),
            preserve_default=False,
        ),
    ]
