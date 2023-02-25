from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import *

# Register your models here.

#Project Model
class ProjectsResourse(resources.ModelResource):
    class Meta:
        model = Projects

class ProjectsAdmin(ImportExportModelAdmin):
    resource_class = ProjectsResourse
admin.site.register(Projects, ProjectsAdmin)

#Events Model
class EventsResourse(resources.ModelResource):
    class Meta:
        model = Events

class EventsAdmin(ImportExportModelAdmin):
    resources_class = EventsResourse
admin.site.register(Events, EventsAdmin)

#Registration Model
class RegistrationResourse(resources.ModelResource):
    class Meta:
        model = Registration

class RegistrationAdmin(ImportExportModelAdmin):
    resources_class = RegistrationResourse
admin.site.register(Registration, RegistrationAdmin)

#Team Model
class TeamResourse(resources.ModelResource):
    class Meta:
        model = Team

class TeamAdmin(ImportExportModelAdmin):
    resources_class = TeamResourse
admin.site.register(Team, TeamAdmin)

#Gallery Model
class GalleryResourse(resources.ModelResource):
    class Meta:
        model = Gallery

class GalleryAdmin(ImportExportModelAdmin):
    resources_class = GalleryResourse
admin.site.register(Gallery, GalleryAdmin)

#Subscriptions Model
class SubscriptionsResourse(resources.ModelResource):
    class Meta:
        model = Subscriptions

class SubscriptionsAdmin(ImportExportModelAdmin):
    resources_class = SubscriptionsResourse
admin.site.register(Subscriptions, SubscriptionsAdmin)
