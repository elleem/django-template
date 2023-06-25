from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Database
from django.shortcuts import render

# Create your views here.
class DatabaseListView(ListView):
    template_name = "list.html"
    model = Database
    context_object_name = "database"

class DatabaseDetailView(DetailView):
    template_name = "detail.html"
    model = Database

class DatabaseCreateView(CreateView):
    template_name = "create.html"
    model = Database
    fields = ["item", "userid", "description", "image_url"]

class DatabaseDeleteView(DeleteView):
    template_name = "delete.html"
    model = Database
    success_url = reverse_lazy("list")

class DatabaseUpdateView(UpdateView):
    template_name = "update.html"
    model = Database
    fields = "__all__"

class AboutView(TemplateView):
    template_name = "about.html"
