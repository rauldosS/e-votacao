from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario
import re

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

    estado = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        label='Estado',
        widget=forms.Select(
            attrs={
                'class': 'custom-select',
            }
        )
    )

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
                    'type': 'text'
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu CPF',
                    'type': 'text',
                    'onfocus': 'javascript: retirarFormatacao(this)',
                    'onblur': 'javascript: formatarCampo(this)',
                    'maxlength': '11',
                }
            ),
            'rg': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe seu RG',
                    'type': 'number'
                }
            )
        }

    def clean_password2(self):
        """ Validação de senha

        Método que valida ambas senhas digitadas no formulário, antes de serem encriptadas e
        guardadas na base de dados, retornando uma senha valida.

        Exception:
        - ValidationError -- quando as senhas não são iguais mostra-ra uma mensagem de erro
        """

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        print('teste')

        if password1 != password2:
            raise forms.ValidationError('Senhas digitadas não são iguais!')

        return password2

    # def clean_cpf(self):
    #     """
    #         Valida CPFs, retornando apenas a string de números válida.
        
    #         # CPFs errados
    #         >>> validar_cpf('abcdefghijk')
    #         False
    #         >>> validar_cpf('123')
    #         False
    #         >>> validar_cpf('')
    #         False
    #         >>> validar_cpf(None)
    #         False
    #         >>> validar_cpf('12345678900')
    #         False
        
    #         # CPFs corretos
    #         >>> validar_cpf('95524361503')
    #         '95524361503'
    #         >>> validar_cpf('955.243.615-03')
    #         '95524361503'
    #         >>> validar_cpf('  955 243 615 03  ')
    #         '95524361503'
    #     """
    #     cpf_ = self.cleaned_data.get('cpf')


    #     cpf = ''.join(re.findall('\d', str(cpf_)))
    
    #     if (not cpf) or (len(cpf) < 11):
    #         return False
    
    #     # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam
    #     inteiros = map(int, cpf)
    #     novo = inteiros[:9]
    
    #     while len(novo) < 11:
    #         r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11
    
    #         if r > 1:
    #             f = 11 - r
    #         else:
    #             f = 0
    #         novo.append(f)
    
    #     # Se o número gerado coincidir com o número original, é válido
    #     if novo == inteiros:
    #         return cpf
    #     else:
    #         raise forms.validationError('CPF inválido!')

    def save(self, commit=True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user