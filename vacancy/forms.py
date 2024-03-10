from django import forms

from vacancy.models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description']

