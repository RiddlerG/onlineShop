# Generated by Django 2.1.7 on 2019-03-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopMenuPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Страница')),
                ('point_url', models.URLField(max_length=250, verbose_name='Ссылка на страницу')),
            ],
            options={
                'verbose_name': 'Пункт верхнего меню',
                'verbose_name_plural': 'Пункты верхнего меню',
            },
        ),
    ]
