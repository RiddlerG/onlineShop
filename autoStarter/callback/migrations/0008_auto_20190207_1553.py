# Generated by Django 2.1.5 on 2019-02-07 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0007_auto_20190207_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='call_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 15, 53, 34, 539352), verbose_name='Время звонка'),
        ),
    ]
