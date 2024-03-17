from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Resume(models.Model):
    CHOICES = (
        ('secondary', 'Secondary'),
        ('specialized secondary', 'Specialized secondary'),
        ('higher', 'Higher'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profession = models.CharField(max_length=255)
    data_of_birth = models.DateField()
    citizenship = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, choices=CHOICES)
    name_of_institution = models.CharField(max_length=255)
    about_your_self = models.TextField()

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

    def get_absolute_url(self):
        return reverse("resume-detail", kwargs={"pk": self.pk})
