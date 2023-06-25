from django.urls import path
from .views import DatabaseListView, DatabaseDetailView, DatabaseCreateView, DatabaseUpdateView, DatabaseDeleteView, AboutView

urlpatterns = [
    path('', DatabaseListView.as_view(), name='list'),
    path('<int:pk>/', DatabaseDetailView.as_view(), name='detail'),
    path('create/', DatabaseCreateView.as_view(), name='create'),
    path('<int:pk>/delete', DatabaseDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', DatabaseUpdateView.as_view(), name='update'),
    path('about', AboutView.as_view(), name='about'),
]