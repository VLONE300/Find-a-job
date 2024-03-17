from django import forms

from resume.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['profession', 'data_of_birth', 'citizenship', 'education_level', 'name_of_institution',
                  'about_your_self']

        widgets = {
            'data_of_birth': forms.SelectDateWidget(years=range(1900, 2024)),
            'education_level': forms.RadioSelect
        }
