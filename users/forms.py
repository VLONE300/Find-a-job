from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Company, JobSeeker


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=True)  # Сначала сохраняем пользователя
        user_type = self.cleaned_data.get('user_type')

        if user_type == 'company':
            Company.objects.create(user=user)
        elif user_type == 'job_seeker':
            JobSeeker.objects.create(user=user)

        return user
