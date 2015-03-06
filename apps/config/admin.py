from django.contrib import admin
from .models import IpAddress, Server, ServiceType, Service, ConfigItem, ConfigValue
from .forms import ConfigItemForm
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

admin.site.register(IpAddress)
admin.site.register(Server)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
