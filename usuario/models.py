from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, name, password=None):
        # , fullname, birth_date, cpf, rg
        # if not email:
        #     raise ValueError('Este usuário não possui e-mail!')
    
        user = self.model(
            username=username,
            # email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, name, password):
        user = self.create_user(
            username=username,
            name=name,
            password=password
        )

        user.user_admin = True
        user.save()

        return user


class Usuario(AbstractBaseUser):
    username = models.IntegerField('Número do título de eleitor', unique=True)
    email = models.EmailField('E-mail', max_length=255, unique=True, null=True)
    name = models.CharField('Nome', max_length=255, blank=True, null=True)
    fullname = models.CharField('Nome completo', max_length=1000, blank=True, null=True)
    # birth_date = models.DateField('Data de nascimento', auto_now=False, default=date.today())
    cpf = models.IntegerField('CPF', blank=True, null=True)
    rg = models.IntegerField('RG', blank=True, null=True)
    # voter_registration_number = models.CharField('Número do título de eleitor', max_length=20)
    nickname = models.CharField('Apelido', max_length=255, blank=True, null=True)
    photo = models.ImageField('Foto de perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200, blank=True, null = True)
    user_active = models.BooleanField('Ativo', default=True)
    user_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.username}, {self.user_active}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label,):
        return True

    @property
    def is_staff(self):
        return self.user_admin

    class Meta:
        ordering = ('id', 'username')