from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
