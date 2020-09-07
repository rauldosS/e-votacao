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
            'placeholder': 'Informe sua senha...',
            'id': 'password1',
            'required': 'required'
        }
    ))

    password2 = forms.CharField(label='Senha de confirmação', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Informe sua senha...',
            'id': 'password2',
            'required': 'required'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username', 'fullname', 'cpf', 'rg')
        widgets = {
            'fullname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu nome completo'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe número do título de eleitor',
                    'type': 'number'
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu CPF',
                    'type': 'number'
                }
            ),
            'rg': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu RG',
                    'type': 'number'
                }
            ),
        }

    def clean_password2(self):
        """ Validação de senha

        Método que valida ambas senhas digitadas no formulário, antes de serem encriptadas e
        guardadas na base de dados, retornando uma senha valida.

        Exception:
        - ValidationError -- quando as senhas não são iguais mostra-ra uma mensagem de erro
        """

        password1 = self.cleaned_data.get['password1']
        password2 = self.cleaned_data.get['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Senhas digitadas não são iguais!')

        return password2
        