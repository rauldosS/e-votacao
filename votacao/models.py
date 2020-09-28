from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


ESTADO_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

class Eleicao(models.Model):
    TIPO_CHOICES = (
        ('Eleição Federal', (
            ('PR', 'Presidentes'),
            ('SN', 'Senadores'),
            ('DF', 'Deputados Federais'),
        )),
        ('Eleição Estadual', (
            ('PR', 'Governadores'),
            ('SN', 'Deputados estaduais'),
        ))
    )

    ano = models.IntegerField('Ano', default=datetime.datetime.now().year)
    tipo = models.CharField('Tipo', default=1, max_length=2, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=2, blank=True, null=True, choices=ESTADO_CHOICES)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Eleição'
        verbose_name_plural = 'Eleições'
        ordering = ('ano', 'tipo')

# Create your models here.
class Candidato(models.Model):
    TIPO_CHOICES = (
        ('PR', 'Presidente'),
        ('SN', 'Senador'),
        ('VR', 'Vereador')
    )

    nome = models.CharField('Nome', max_length=255)
    nascimento = models.DateField('Data de nascimento', auto_now=False, default=timezone.now)
    titulo = models.CharField('Título', default=1, max_length=2, choices=TIPO_CHOICES)
    estado = models.CharField('Estado', default=1, max_length=2, choices=ESTADO_CHOICES)
    foto = models.ImageField('Foto de perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200, blank=True, null = True)

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ('nome', 'nascimento')

class Turno(models.Model):
    turno = models.IntegerField('Turno', default='1')
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    dat_ini = models.DateField('Data inicío', auto_now=False, default=timezone.now)
    dat_fim = models.DateField('Data fim', auto_now=False, default=timezone.now)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ('dat_ini', 'dat_fim')