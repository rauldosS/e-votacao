# Generated by Django 3.1.1 on 2020-09-28 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0020_auto_20200928_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrovotacao',
            name='eleicao',
        ),
        migrations.AlterField(
            model_name='registrovotacao',
            name='turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacao.votacaoturnocandidato'),
        ),
    ]
