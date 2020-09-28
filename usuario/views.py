from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from usuario.models import Usuario
from usuario.forms import FormularioLogin, FormularioUsuario

# Create your views here.
def home(request):
    title = 'Dados do usuário'

    return render(request, 'usuarios/home.html', {'title': title})

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    # def logout(self, request):
    #     logout(self.request)
    #     return HttpResponseRedirect('/account/login/')

class ListaUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuarios.html'

    def get_queryset(self):
        return self.model.objects.filter(user_active=True)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/registrar_usuario.html'

    success_url = reverse_lazy('usuarios:listar_usuarios')

class CadastroUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/cadastro.html'

    success_url = reverse_lazy('login')