from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method.decorator
from django.views.decorators.csrf import csrf.project
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin

# Create your views here.
class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_project)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logout(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')