from django.contrib import admin
from .models import HttpHost

class HttpHostAdmin(admin.ModelAdmin):
    list_display = [ 'domain', 'php', 'usessl' ]
    fieldsets = (
            (None, {
                'fields': [ 'domain', 'php' ]
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
