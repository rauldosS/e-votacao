from django.shortcuts import render
import requests
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from votacao.models import Candidato, Turno, Eleicao, VotacaoTurnoCandidato, RegistroVotacao
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.db.models import Q
# from django.contrib.auth.models import User
import json

module = 'Resultados'

# Create your views here.
@login_required
def home(request):
    title = 'Resultados'

    datas = get_datas(request)

    return render(request, 'resultado/home.html', {'title': title, 'module': module, 'datas': datas})

def get_datas(request):
    pass
#     expenses = Expense.objects.filter(~Q(paid_out=True), user=request.user, date_expense__year=datetime.now().year)
#     incomes = Income.objects.filter(user=request.user, dt_inicial__year=datetime.now().year)
#     parcels = Parcel.objects.filter(expense__in=(expenses), date__year=datetime.now().year)
    
#     datas  = {
#         'Rendimentos': {'values': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'color': '#27ae60'},
#         'Despesas': {'values': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'color': '#ee5253'}
#     }

#     for parcel in parcels:
#         datas['Despesas']['values'][int(parcel.date.strftime('%m')) - 1] += float(parcel.value)

#     for income in incomes:
#         datas['Rendimentos']['values'][int(income.dt_inicial.strftime('%m')) - 1] += float(income.value_income)

#     return datas