from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.IntegerField(verbose_name='телефон', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='город')
    avatar = models.ImageField(upload_to='avatar/', verbose_name='аватарка', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
