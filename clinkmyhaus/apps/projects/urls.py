"""Projects URLs."""

from django.urls import path

from clinkmyhaus.apps.projects.views import ProjectDetailView, ProjectListView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('proyectos/<slug:slug>/', ProjectDetailView.as_view(), name='detail'),
]
