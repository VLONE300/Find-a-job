from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import register_view, profile_view

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]
