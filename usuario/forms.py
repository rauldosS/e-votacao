from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha'

class FormularioUsuario(forms.ModelForm):
    """ Formulário de Registro de um usuário na base de dados

    Variables:

        - password1: senha
        - password2: verificação de senha

    """
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder'='Informe sua senha...',
            'id': 'password1',
            'required': 'required'
        }
    ))

    password2 = forms.CharField(label='Senha de confirmação', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder'='Informe sua senha...',
            'id': 'password2',
            'required': 'required'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'name', 'nickname')
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu nome'
                }
            ),
            'nickname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu apelido'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu nome de usuário'
                }
            )
        }