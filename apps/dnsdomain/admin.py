from django.contrib import admin
from .models import DnsDomain, DnsRecord
from ..common.admin import ACSModelAdmin

class DnsRecordInline(admin.TabularInline):
    model = DnsRecord
    extra = 0
    fieldsets = (
            (None, {
                'fields': [ 'name', 'type', 'content', 'ttl', 'prio', 'enabled', 'user' ]
                }),
            )

class DnsDomainAdmin(ACSModelAdmin):
    inlines = [ DnsRecordInline, ]
    list_display = [ 'domain', 'type', 'get_users', 'enabled' ]
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'type', 'user' )
                }),
            ('Slave options', {
                'classes': ('collapse',),
                'fields': [ 'master' ]
                }),
            )

    def save_model(self, request, obj, form, change):
        super(DnsDomainAdmin, self).save_model(request, obj, form, change)
        obj.save()

admin.site.register(DnsDomain, DnsDomainAdmin)
