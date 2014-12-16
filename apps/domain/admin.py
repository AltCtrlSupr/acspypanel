from django.contrib import admin
from .models import Domain
from ..common.admin import ACSModelAdmin

class DomainAdmin(ACSModelAdmin):
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'user', 'enabled' )
                }),
            )
    list_display = [ 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'get_users', 'enabled' ]

admin.site.register(Domain, DomainAdmin)
