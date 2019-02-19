# Generated by Django 2.1.7 on 2019-02-16 11:24

import brands.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default=1, upload_to=brands.models.Brand.get_picture_url, verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
