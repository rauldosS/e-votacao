from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

title = 'Início'

# Create your views here.
@login_required
def home(request):
    teste = 'ok'

    return render(request, 'home/home.html', {'title': title, 'teste': teste})