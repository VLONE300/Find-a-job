from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import profile_view

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/',LogoutView.as_view(), name='logout')
]