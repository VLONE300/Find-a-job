from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from resume.models import Resume
from vacancy.forms import VacancyForm, VacancyFilterForm
from vacancy.models import Vacancy, VacancyApplication


# Create your views here.
class VacancyListView(ListView):
    model = Vacancy
    queryset = Vacancy.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        form = VacancyFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['search']:
                queryset = queryset.filter(title__icontains=form.cleaned_data['search'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VacancyFilterForm(self.request.GET)
        return context


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
    success_url = reverse_lazy('users:profile')

    def get_queryset(self):
        return Vacancy.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs['pk'])


class DeleteVacancyView(LoginRequiredMixin, View):
    def get(self, request, pk):
        Vacancy.objects.filter(pk=pk, user=request.user).delete()
        return redirect('users:profile')


class ApplyVacancyView(LoginRequiredMixin, View):
    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        job_seeker = request.user
        resume = Resume.objects.filter(user=job_seeker).first()
        existing_application = VacancyApplication.objects.filter(vacancy=vacancy, job_seeker=job_seeker).exists()
        if existing_application:
            messages.error(request, "You've already applied to this vacancy.")
            return redirect(vacancy.get_absolute_url())
        else:
            VacancyApplication.objects.create(vacancy=vacancy, job_seeker=job_seeker, resume=resume)
            messages.success(request, "Your application has been submitted successfully")
            return redirect(vacancy.get_absolute_url())

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
