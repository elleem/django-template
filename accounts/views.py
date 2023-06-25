from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class HomeView(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle successful user registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Handle successful profile update
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'pages/profile_edit.html', {'form': form})