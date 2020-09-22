from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

title = 'Controle'

# Create your views here.
@login_required
def home(request):
    teste = 'ok'

    return render(request, 'controle/home.html', {'title': title, 'teste': teste})