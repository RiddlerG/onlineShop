# Generated by Django 2.1.5 on 2019-01-21 13:27

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isMain', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('image', models.ImageField(upload_to=shop.models.Image.get_picture_url, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('price_without_sale', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Цена без скидки')),
                ('sale', models.PositiveIntegerField(default=0, verbose_name='Скидка')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Цена')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Описание')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='На складе')),
                ('published', models.BooleanField(default=True, verbose_name='Активно')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Product', verbose_name='Товар'),
        ),
    ]
