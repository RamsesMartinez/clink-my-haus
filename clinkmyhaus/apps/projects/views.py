from django.views.generic.list import ListView

from clinkmyhaus.apps.projects.models.projects import Project


class ProjectListView(ListView):
    model = Project
    paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_pic'] = self.model
        return context
