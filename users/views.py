from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from resume.models import Resume
from users.forms import RegistrationForm, CompanyForm, JobSeekerForm
from vacancy.models import Vacancy, VacancyApplication


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user_type = form.cleaned_data['user_type']
            if user_type == 'company':
                company_form = CompanyForm(request.POST)
                if company_form.is_valid():
                    company = company_form.save(commit=False)
                    company.user = user
                    company.save()
            elif user_type == 'job_seeker':
                job_seeker_form = JobSeekerForm(request.POST)
                if job_seeker_form.is_valid():
                    job_seeker = job_seeker_form.save(commit=False)
                    job_seeker.user = user
                    job_seeker.save()

            return redirect('login')

        return render(request, 'registration/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        vacancies = Vacancy.objects.filter(user=request.user)
        resumes = Resume.objects.filter(user=request.user)
        feedbacks = VacancyApplication.objects.filter(vacancy_id__user=request.user)
        return render(request, 'users/profile.html',
                      context={'vacancies': vacancies, 'resumes': resumes, "feedbacks": feedbacks})
