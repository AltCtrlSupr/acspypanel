from django.contrib import admin
from .models import HttpHost
from ..common.admin import ACSModelAdmin

class HttpHostAdmin(ACSModelAdmin):
    list_display = [ 'domain', 'php', 'usessl', 'user' ]
    fieldsets = (
            (None, {
                'fields': [ 'domain', 'php', 'user' ]
                }),
            ('Extra', {
                'classes' : ('collapse',),
                'fields' : [ 'configuration' ]
                }),
            ('SSL', {
                'classes' : ('collapse',),
                'fields' : [ 'usessl', 'certificate', 'certificate_key', 'certificate_chain', 'certificate_authority' ]
                }),
            )

admin.site.register(HttpHost, HttpHostAdmin)
