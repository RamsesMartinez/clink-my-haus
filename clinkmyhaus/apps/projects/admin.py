from django.contrib import admin
from clinkmyhaus.apps.projects.models.projects import Project, ProjectRenders, ProjectConstructionPlans
from clinkmyhaus.apps.projects.models.addresses import State, TownHall, Suburb


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name',)
    list_display_links = ('id', 'state_name',)
    ordering = ('created', 'state_name')


@admin.register(TownHall)
class TownHallAdmin(admin.ModelAdmin):
    list_display = ('id', 'town_hall_name',)
    list_display_links = ('id', 'town_hall_name',)
    ordering = ('created', 'town_hall_name')


@admin.register(Suburb)
class SuburbAdmin(admin.ModelAdmin):
    list_display = ('id', 'suburb_name',)
    list_display_links = ('id', 'suburb_name',)
    ordering = ('created', 'suburb_name')


class ProjectImageInline(admin.StackedInline):
    model = ProjectRenders


class ProjectConstructionPlansInline(admin.StackedInline):
    model = ProjectConstructionPlans


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'slug')
    list_display_links = ('id', 'project_name', 'slug')
    ordering = ('created', 'project_name')
    inlines = [ProjectImageInline, ProjectConstructionPlansInline]
