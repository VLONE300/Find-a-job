from django import forms
from .models import CustomUser, Company, JobSeeker


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_type']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name']


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['first_name', 'last_name']
