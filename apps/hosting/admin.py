from django.contrib import admin
from .models import Plan, Hosting, HostingPlan, Resource, PlanResource
from ..common.admin import ACSModelAdmin


class HostingPlanInline(admin.TabularInline):
    model = HostingPlan
    extra = 1
    fieldsets = (
            (None, {
                'fields': [ 'plan' ]
                }),
            )

class HostingAdmin(ACSModelAdmin):
    inlines = [ HostingPlanInline, ]
    list_display = [ 'name', 'get_plans', 'get_resources' ]

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


admin.site.register(Hosting, HostingAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Resource)
