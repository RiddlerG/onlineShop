# Generated by Django 2.1.5 on 2019-01-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20190120_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='name',
            field=models.CharField(default=2, max_length=250, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
