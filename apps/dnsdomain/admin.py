from django.contrib import admin
from .models import DnsDomain, DnsRecord
from ..common.admin import ACSModelAdmin

class DnsRecordInline(admin.TabularInline):
    model = DnsRecord
    extra = 0
    fieldsets = (
            (None, {
                'fields': [ 'name', 'type', 'content', 'ttl', 'prio', 'enabled' ]
                }),
            )

class DnsDomainAdmin(ACSModelAdmin):
    inlines = [ DnsRecordInline, ]
    list_display = [ 'domain', 'type', 'get_users', 'enabled' ]
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'type' )
                }),
            ('Slave options', {
                'classes': ('collapse',),
                'fields': [ 'master' ]
                }),
            )

admin.site.register(DnsDomain, DnsDomainAdmin)
