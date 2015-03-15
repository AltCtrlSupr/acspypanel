from django.contrib import admin
from .models import Plan, Hosting, HostingPlan, Resource, PlanResource
from ..settings.models import SettingValue
from ..common.admin import ACSModelAdmin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline


class HostingPlanInline(admin.TabularInline):
    model = HostingPlan
    extra = 1
    fieldsets = (
            (None, {
                'fields': [ 'plan' ]
                }),
            )

class SettingValueInline(GenericTabularInline):
    model = SettingValue
    ct_field = 'scope'


class HostingAdmin(ACSModelAdmin):
    inlines = [ HostingPlanInline, SettingValueInline ]
    list_display = [ 'name', 'get_plans', 'get_resources', 'get_used_resources' ]

class PlanResourceInline(admin.TabularInline):
    model = PlanResource
    extra = 0
    fieldsets = (
            (None, {
                'fields' : [ 'resource', 'value' ],
                }),
            )

class PlanAdmin(ACSModelAdmin):
    inlines = [ PlanResourceInline, ]
    fieldsets = (
            (None, {
                'fields' : [ 'name', 'enabled' ],
                }),
            )

class ResourceAdmin(ACSModelAdmin):
    list_display = [ 'name', 'description', 'default', 'content_type', 'enabled' ]
    fieldsets = (
            (None, {
                'fields' : [ 'name', 'description', 'default', 'content_type', 'enabled' ],
                }),
            )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(ResourceAdmin, self).get_readonly_fields(request, obj)
        return ['content_type'] if obj is not None and obj.pk else []

    def get_form(self, request, obj=None, **kwargs):
        form = super(ResourceAdmin, self).get_form(request, obj,**kwargs)
        if not obj:
            # change the manager to show only valid id to avoid have two queries
            form.base_fields['content_type'].queryset = form.base_fields['content_type'].queryset.filter(id__in=[c.id for c in Resource.objects.resource_models()]).exclude(id__in=[resource.content_type.id for resource in Resource.objects.all()])
        return form

admin.site.register(Hosting, HostingAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Resource, ResourceAdmin)
