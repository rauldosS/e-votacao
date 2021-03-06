# Generated by Django 3.0.8 on 2020-09-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0016_auto_20200928_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleicao',
            name='tipo',
            field=models.CharField(choices=[('Eleição Federal', (('PR', 'Presidente'), ('SN', 'Senador'), ('DF', 'Deputado Federal'))), ('Eleição Estadual', (('GV', 'Governador'), ('DE', 'Deputado estadual')))], default=1, max_length=2, verbose_name='Tipo'),
        ),
    ]
