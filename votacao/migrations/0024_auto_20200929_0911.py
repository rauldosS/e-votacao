# Generated by Django 3.0.8 on 2020-09-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0023_auto_20200929_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrovotacao',
            name='candidato',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registrovotacao',
            name='eleicao',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registrovotacao',
            name='turno',
            field=models.IntegerField(),
        ),
    ]