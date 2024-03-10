from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
