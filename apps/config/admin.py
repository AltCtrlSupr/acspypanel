from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import IpAddress, Server, ServiceType, Service, ConfigItem, ConfigValue
from ..common.admin import ACSModelAdmin

class ConfigItemInline(admin.TabularInline):
    model = ConfigItem

class ServiceTypeAdmin(ACSModelAdmin):
    inlines = [ ConfigItemInline, ]

class ConfigValueInline(admin.TabularInline):
    model = ConfigValue
    extra = 0
    max_num = 0
    fields = [ 'value' ]

class ServiceAdmin(ACSModelAdmin):
    inlines = [ ConfigValueInline, ]

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("../%s" % obj.id)

admin.site.register(IpAddress)
admin.site.register(Server)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
