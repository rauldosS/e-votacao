from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('Este usuário não possui e-mail!')
    
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            password=password
        )

        user.user_admin = True
        user.save()

        return user


class Usuario(AbstractBaseUser):
    username = models.CharField('Nome de usuário', unique=True, max_length=50)
    email = models.EmailField('E-mail', max_length=255, unique=True)
    name = models.CharField('Nome', max_length=255, blank=True, null=True)
    nickname = models.CharField('Apelido', max_length=255, blank=True, null=True)
    photo = models.ImageField('Foto de perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200, blank=True, null = True)
    user_active = models.BooleanField(default=True)
    user_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return f'{self.username}, {self.user_active}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label,):
        return True

    @property
    def is_staff(self):
        return self.user_admin