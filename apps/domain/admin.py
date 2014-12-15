from django.contrib import admin
from .models import Domain

class DomainAdmin(admin.ModelAdmin):
    list_display = [ 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias' ]
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'user', 'enabled' )
                }),
            )

admin.site.register(Domain, DomainAdmin)
