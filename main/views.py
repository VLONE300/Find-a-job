from django.views import View
from django.shortcuts import render
from vacancy.models import Vacancy
from resume.models import Resume


class MainPageView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        resumes = Resume.objects.all()
        return render(request, 'main/main.html', {'vacancies': vacancies, 'resumes': resumes})
