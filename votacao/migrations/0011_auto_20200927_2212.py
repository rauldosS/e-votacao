# Generated by Django 3.1.1 on 2020-09-28 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0010_auto_20200927_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eleicao',
            options={'ordering': ('ano', 'tipo'), 'verbose_name': 'Eleição', 'verbose_name_plural': 'Eleições'},
        ),
    ]
