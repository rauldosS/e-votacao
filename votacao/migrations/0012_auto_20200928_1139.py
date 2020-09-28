# Generated by Django 3.0.8 on 2020-09-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0011_auto_20200927_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='numero',
            field=models.IntegerField(default=0, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido',
            field=models.CharField(choices=[('PSDB', 'Partido da Social Democracia Brasileira'), ('PP', 'Progressistas'), ('Partido Democrático Trabalhista', 'PDT'), ('Partido Trabalhista Brasileiro', 'PTB'), ('TT', 'Teste')], default=2, max_length=255, verbose_name='Partido'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='turno',
            name='candidatos',
            field=models.ManyToManyField(related_name='candidatos', to='votacao.Candidato', verbose_name='Candidatos'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='titulo',
            field=models.CharField(choices=[('Eleição Federal', (('PR', 'Presidente'), ('SN', 'Senador'), ('DF', 'Deputado Federal'))), ('Eleição Estadual', (('GV', 'Governador'), ('DE', 'Deputado estadual')))], default=1, max_length=2, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='eleicao',
            name='tipo',
            field=models.CharField(choices=[('Eleição Federal', (('PR', 'Presidentes'), ('SN', 'Senadores'), ('DF', 'Deputados Federais'))), ('Eleição Estadual', (('GV', 'Governadores'), ('DE', 'Deputados estaduais')))], default=1, max_length=2, verbose_name='Tipo'),
        ),
    ]
