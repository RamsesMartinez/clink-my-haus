from django.views.generic import DetailView
from django.views.generic.list import ListView

from clinkmyhaus.apps.projects.models.addresses import State
from clinkmyhaus.apps.projects.models.projects import Project

import logging


class ProjectsByStateListView(ListView):
    model = State
    context_object_name = 'projects_by_state_list'
    template_name = 'projects/projects_by_state_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_pic'] = self.model
        return context

    def get_queryset(self):
        """Filter by price if it is provided in GET parameters"""
        queryset = super(ProjectsByStateListView, self).get_queryset()
        queryset = queryset.prefetch_related('townhall_set', 'townhall_set__suburb_set__project_set')
        return queryset


class ProjectDetailView(DetailView):
    model = Project
