from django.contrib import admin
from clinkmyhaus.apps.projects.models.projects import Project
from clinkmyhaus.apps.projects.models.addresses import State, Locality


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name',)
    list_display_links = ('id', 'state_name',)
    ordering = ('created', 'state_name')


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'locality_name',)
    list_display_links = ('id', 'locality_name',)
    ordering = ('created', 'locality_name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name',)
    list_display_links = ('id', 'project_name',)
    ordering = ('created', 'project_name')


