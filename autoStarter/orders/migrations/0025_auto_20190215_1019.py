# Generated by Django 2.1.7 on 2019-02-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20190214_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Комментарий'),
        ),
    ]
