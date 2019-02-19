# Generated by Django 2.1.5 on 2019-02-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190207_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Посчитается при сохранении.', max_digits=10, null=True, verbose_name='Итоговая стоимость'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Посчитается при сохранении.', max_digits=10, null=True, verbose_name='Стоимость'),
        ),
    ]
