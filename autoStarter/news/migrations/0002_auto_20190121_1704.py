# Generated by Django 2.1.5 on 2019-01-21 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='news',
            index_together={('id', 'slug')},
        ),
    ]
