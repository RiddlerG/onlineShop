# Generated by Django 2.1.5 on 2019-02-13 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20190213_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='isMain',
            new_name='is_main',
        ),
    ]
