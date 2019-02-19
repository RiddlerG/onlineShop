# Generated by Django 2.1.5 on 2019-02-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20190213_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('cash', 'Наличный расчёт'), ('card', 'Оплата картой')], max_length=250, verbose_name='Способ оплаты'),
        ),
    ]
