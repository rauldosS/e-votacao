# Generated by Django 3.1 on 2020-09-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0018_auto_20200905_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.IntegerField(blank=True, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fullname',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Nome completo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rg',
            field=models.IntegerField(blank=True, null=True, verbose_name='RG'),
        ),
    ]
