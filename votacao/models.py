from django.db import models
import datetime
from django.utils import timezone
from usuario.models import Usuario
from django.conf import settings

TIPO_CHOICES = (
    ('Eleição Federal', (
        ('PR', 'Presidente'),
        ('SN', 'Senador'),
        ('DF', 'Deputado Federal'),
    )),
    ('Eleição Estadual', (
        ('GV', 'Governador'),
        ('DE', 'Deputado estadual'),
    ))
)

PARTIDO_CHOICES = (
    ('PSDB', 'Partido da Social Democracia Brasileira'),
    ('PP', 'Progressistas'),
    ('Partido Democrático Trabalhista', 'PDT'),
    ('Partido Trabalhista Brasileiro', 'PTB'),
    ('TT', 'Teste'),
)

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
    ano = models.IntegerField('Ano', default=datetime.datetime.now().year)
    tipo = models.CharField('Tipo', default=1, max_length=2, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=2, blank=True, null=True, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'{self.tipo}, {self.ano}'

    class Meta:
        verbose_name = 'Eleição'
        verbose_name_plural = 'Eleições'
        ordering = ('id', 'ano', 'tipo')

# Create your models here.
class Candidato(models.Model):
    nome = models.CharField('Nome', max_length=255)
    nascimento = models.DateField('Data de nascimento', auto_now=False, default=timezone.now)
    titulo = models.CharField('Título', default=1, max_length=2, choices=TIPO_CHOICES)
    partido = models.CharField('Partido', max_length=255, choices=PARTIDO_CHOICES)
    numero = models.IntegerField('Número', default=0000)
    estado = models.CharField('Estado', default=1, max_length=2, choices=ESTADO_CHOICES)
    foto = models.ImageField('Foto de perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200, blank=True, null = True)
    
    def __str__(self):
        return f'{self.nome}, {self.titulo}, {self.partido}'
    
    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ('id', 'nome', 'nascimento')

class Turno(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    turno = models.IntegerField('Turno', default='1')
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    dat_ini = models.DateField('Data inicío', auto_now=False, default=timezone.now)
    dat_fim = models.DateField('Data fim', auto_now=False, default=timezone.now)
    candidatos = models.ManyToManyField(Candidato, verbose_name='Candidatos', related_name='candidatos')

    def __str__(self):
        return f'{self.eleicao}, {self.turno}, {self.dat_ini}, {self.dat_fim}'

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ('id', 'dat_ini', 'dat_fim')

class VotacaoTurnoCandidato(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    votos = models.IntegerField(default=0, blank=True, null = True, editable=False)

    def __str__(self):
        return f'{self.id}, {self.turno}, {self.candidato}'

    class Meta:
        verbose_name = 'Votação por turno por candidato'
        verbose_name_plural = 'Votações por turno por candidato'
        ordering = ('id', 'turno', 'candidato')

class RegistroVotacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    usuario = models.IntegerField()
    eleicao = models.IntegerField()
    turno = models.IntegerField()
    candidato = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True, blank=True)

    

    class Meta:
        verbose_name = 'Registro de votação'
        verbose_name_plural = 'Registro de votações'
        ordering = ('id', 'turno', 'candidato')