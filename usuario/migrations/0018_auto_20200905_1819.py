# Generated by Django 3.1 on 2020-09-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0017_auto_20200905_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True, verbose_name='E-mail'),
        ),
    ]