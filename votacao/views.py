from django.shortcuts import render
from votacao.models import Candidato, Turno, Eleicao
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def home(request):
    title = 'e-Votação'

    """
        Eleições por turno por tipo

        Exibe eleições do estado de cadastro do eleitor e também eleições que não possuem estado associado (federais)
    """

    data = {}

    eleicoes = Eleicao.objects.filter((Q(estado=request.user.estado) | Q(estado=None)), ano__gte=int(datetime.now().year))
    turnos = Turno.objects.filter(eleicao__in=(eleicoes), ativo=True)

    print(eleicoes)

    for eleicao in eleicoes:
        try:
            turnos_eleicao = Turno.objects.filter(eleicao=eleicao.id)
            color = ''
            font_color = ''

            for turno in turnos_eleicao:
                if (eleicao.get_tipo_display() == 'Presidentes') or (eleicao.get_tipo_display() == 'Senadores') or (eleicao.get_tipo_display() == 'Deputados Federais'):
                    color = 'success'
                elif (eleicao.get_tipo_display() == 'Governadores') or (eleicao.get_tipo_display() == 'Deputados estaduais'):
                    color = 'danger'
                    
                
                data.update({
                    eleicao.id: {
                        'turno': turno.id,
                        'dat_ini': turno.dat_ini, 
                        'dat_fim': turno.dat_fim,
                        'tipo': eleicao.get_tipo_display(),
                        'color': color,
                    } 
                })
        
        except Turno.DoesNotExist:
            print('não contém turno')
        
    print(data)

    return render(request, 'votacao/home.html', {'title': title, 'eleicoes': data})