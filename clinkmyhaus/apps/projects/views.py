from django.views.generic import DetailView
from django.views.generic.list import ListView

from clinkmyhaus.apps.projects.models.projects import Project

import logging


class ProjectListView(ListView):
    model = Project
    paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_pic'] = self.model
        return context

    def get_queryset(self):
        """Filter by price if it is provided in GET parameters"""
        queryset = super(ProjectListView, self).get_queryset()
        queryset = queryset.select_related('suburb', 'suburb__town_hall', 'suburb__town_hall__state')
        return queryset


class ProjectDetailView(DetailView):
    model = Project
