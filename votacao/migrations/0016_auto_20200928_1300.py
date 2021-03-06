# Generated by Django 3.0.8 on 2020-09-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0015_auto_20200928_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={'ordering': ('id', 'dat_ini', 'dat_fim'), 'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
        migrations.AlterField(
            model_name='votacaoturnocandidato',
            name='votos',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
