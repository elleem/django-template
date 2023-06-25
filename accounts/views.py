from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Database

from .forms import CustomUserCreationForm, CustomUserChangeForm

class HomeView(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class DatabaseListView(ListView):
    template_name = "pages/list.html"
    model = Database
    context_object_name = "items"

class DatabaseDetailView(DetailView):
    template_name = "pages/detail.html"
    model = Database

class DatabaseCreateView(CreateView):
    template_name = "pages/create.html"
    model = Database
    fields = ["item", "userid", "description", "image_url"]

class DatabaseDeleteView(DeleteView):
    template_name = "pages/delete.html"
    model = Database
    success_url = reverse_lazy("pages/list")

class DatabaseUpdateView(UpdateView):
    template_name = "pages/update.html"
    model = Database
    fields = "__all__"

class AboutView(TemplateView):
    template_name = "pages/about.html"


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'pages/profile_edit.html', {'form': form})