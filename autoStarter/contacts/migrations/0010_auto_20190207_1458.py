# Generated by Django 2.1.5 on 2019-02-07 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20190207_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sociallink',
            options={'verbose_name': 'Социальная сеть', 'verbose_name_plural': 'Социальные сети'},
        ),
        migrations.RemoveField(
            model_name='sociallink',
            name='phone',
        ),
    ]
