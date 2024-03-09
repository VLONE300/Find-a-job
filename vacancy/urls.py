from django.urls import path

from vacancy.views import VacancyListView

urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy-list')
]
