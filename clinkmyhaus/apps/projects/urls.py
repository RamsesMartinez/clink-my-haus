"""Projects URLs."""

# Django

from django.urls import path

from clinkmyhaus.apps.projects.views import ProjectListView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
]
