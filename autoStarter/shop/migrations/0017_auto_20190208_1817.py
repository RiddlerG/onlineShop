# Generated by Django 2.1.5 on 2019-02-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20190208_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='Заполнится при сохранении', max_length=250, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Посчитается при сохранении', max_digits=10, verbose_name='Цена'),
        ),
    ]
