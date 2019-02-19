# Generated by Django 2.1.5 on 2019-02-10 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20190208_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('value', models.CharField(max_length=250, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250, verbose_name='Значение')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Feature', verbose_name='Характеристика')),
            ],
            options={
                'verbose_name': 'Значение',
                'verbose_name_plural': 'Значения',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Feature', verbose_name='Характеристики'),
        ),
    ]
