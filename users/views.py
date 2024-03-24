from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from resume.models import Resume
from vacancy.models import Vacancy, VacancyApplication
from users.forms import CustomUserCreationForm


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        vacancies = Vacancy.objects.filter(user=request.user)
        resumes = Resume.objects.filter(user=request.user)
        feedbacks = VacancyApplication.objects.filter(vacancy_id__user=request.user)
        return render(request, 'users/profile.html',
                      context={'vacancies': vacancies, 'resumes': resumes, "feedbacks": feedbacks})
