from django.urls import path

from vacancy.views import AddVacancyView, VacancyListView, VacancyView, EditVacancyView,DeleteVacancyView,ApplyVacancyView

urlpatterns = [
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy-detail'),
    path('vacancy/create', AddVacancyView.as_view(), name='create-vacancy'),
    path('vacancy/<int:pk>/edit/', EditVacancyView.as_view(), name='edit-vacancy'),
    path('vacancy/<int:pk>/delete/', DeleteVacancyView.as_view(), name='delete-vacancy'),
    path('vacancy/<int:pk>/apply/', ApplyVacancyView.as_view(), name='apply-vacancy'),

]
