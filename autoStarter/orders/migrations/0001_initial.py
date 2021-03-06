# Generated by Django 2.1.5 on 2019-01-21 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0006_auto_20190121_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=250, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('postcode', models.CharField(max_length=20, verbose_name='Индекс')),
                ('city', models.CharField(max_length=250, verbose_name='Город')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая цена')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
                'ordering': ['order'],
            },
        ),
    ]
