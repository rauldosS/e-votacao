# Generated by Django 3.0.8 on 2020-09-28 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0019_registrovotacao_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrovotacao',
            options={'ordering': ('id', 'turno', 'candidato'), 'verbose_name': 'Registro de votação', 'verbose_name_plural': 'Registro de votações'},
        ),
    ]
