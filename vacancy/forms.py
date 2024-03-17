from django import forms

from vacancy.models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description']

class VacancyFilterForm(forms.Form):
    search = forms.CharField(max_length=255,required=False)


