from django.conf import settings
from django.db import models
from django.urls import reverse

from resume.models import Resume


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def get_absolute_url(self):
        return reverse("vacancy-detail", kwargs={"pk": self.pk})


class VacancyApplication(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
