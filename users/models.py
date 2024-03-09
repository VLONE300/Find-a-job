from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    USER = '1', 'User'
    ADMIN = '2', 'Admin'
    COMPANY = '3', 'Company'


class CustomUser(AbstractUser):
    role = models.IntegerField(choices=Role.choices, default=Role.USER)
