# Generated by Django 3.1.1 on 2020-09-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0008_auto_20200927_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleicaoestadual',
            name='ano',
            field=models.IntegerField(default=2020, verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='eleicaofederal',
            name='ano',
            field=models.IntegerField(default=2020, verbose_name='Ano'),
        ),
    ]
