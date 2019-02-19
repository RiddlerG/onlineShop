# Generated by Django 2.1.7 on 2019-02-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_auto_20190217_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='release_date',
        ),
        migrations.AddField(
            model_name='car',
            name='release_date',
            field=models.PositiveSmallIntegerField(default=2011, verbose_name='Год выпуска'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CarRelease',
        ),
    ]
