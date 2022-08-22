from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .managers import CustomUserManager

ROLES = [
    ('user', 'Аутентифицированный пользователь'),
    ('moderator', 'Модератор'), ('admin', 'Администратор'),
    ('superuser', 'Суперюзер Django')
]


class User(AbstractBaseUser):
    """Кастомная модель пользователя"""
    username = models.CharField(max_length=150, unique=True,
                                validators=[UnicodeUsernameValidator],)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        choices=ROLES, max_length=35, default='user'
    )
    confirmation_code = models.CharField(max_length=50, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role', 'confirmation_code']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'
