# Generated by Django 2.1.7 on 2019-03-12 12:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_auto_20190312_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
    ]
