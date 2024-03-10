from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from vacancy.forms import VacancyForm
from vacancy.models import Vacancy


# Create your views here.
class MainView(ListView):
    model = Vacancy
    queryset = Vacancy.objects.all()


class VacancyView(DetailView):
    model = Vacancy
    slug_field = 'pk'


class AddVacancyView(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "vacancy/add_vacancy.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditVacancyView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = "vacancy/edit_vacancy.html"
    success_url = reverse_lazy('vacancy-list')

    def get_queryset(self):
        return Vacancy.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs['pk'])
