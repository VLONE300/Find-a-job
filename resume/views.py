from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from resume.forms import ResumeForm
from resume.models import Resume


class ResumeListView(ListView):
    model = Resume
    queryset = Resume.objects.all()


class ResumeView(DetailView):
    model = Resume
    slug_field = 'pk'


class AddResumeView(CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = "resume/add_resume.html"
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = self.request.user
        if Resume.objects.filter(user=user).exists():
            return redirect('users:profile')
        else:
            form.instance.user = self.request.user
            return super().form_valid(form)


class EditResumeView(LoginRequiredMixin, UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = "resume/edit_resume.html"
    success_url = reverse_lazy('users:profile')

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs['pk'])


class DeleteResumeView(View):
    def get(self, request, pk):
        Resume.objects.filter(pk=pk, user=request.user).delete()
        return redirect('users:profile')

