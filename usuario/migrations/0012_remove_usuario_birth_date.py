# Generated by Django 3.0.8 on 2020-09-03 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_auto_20200903_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='birth_date',
        ),
    ]
