from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('company', 'Company'),
        ('job_seeker', 'Job Seeker'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
