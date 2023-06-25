from django.urls import path

from .views import SignUpView, profile_edit, DatabaseListView, DatabaseDetailView, AboutView, DatabaseCreateView, DatabaseUpdateView, DatabaseDeleteView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('', DatabaseListView.as_view(), name='list'),
    path('<int:pk>/', DatabaseDetailView.as_view(), name='detail'),
    path('create/', DatabaseCreateView.as_view(), name='create'),
    path('<int:pk>/delete', DatabaseDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', DatabaseUpdateView.as_view(), name='update'),
    path('about', AboutView.as_view(), name='about'),
]