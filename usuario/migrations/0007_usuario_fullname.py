# Generated by Django 3.0.8 on 2020-09-03 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_auto_20200903_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fullname',
            field=models.CharField(max_length=1000, null=True, verbose_name='Nome completo'),
        ),
    ]
