from django.urls import path

from vacancy.views import AddVacancyView, MainView, VacancyView, EditVacancyView

urlpatterns = [
    path('', MainView.as_view(), name='vacancy-list'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy-detail'),
    path('vacancy/create', AddVacancyView.as_view(), name='create-vacancy'),
    path('news/<int:pk>/edit/', EditVacancyView.as_view(), name='edit-vacancy'),

]
