from django.contrib import admin
from .models import Domain
from ..common.admin import ACSModelAdmin
from ..httphost.models import HttpHost

class DomainAdmin(ACSModelAdmin):
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'user', 'enabled' )
                }),
            )
    list_display = [ 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'get_users', 'enabled' ]

class DomainWizard(Domain):
    class Meta:
        proxy = True

class HttpHostInline(admin.StackedInline):
    model = HttpHost

class DomainWizardAdmin(DomainAdmin):
    inlines = [ HttpHostInline, ]

admin.site.register(Domain, DomainAdmin)
admin.site.register(DomainWizard, DomainWizardAdmin)
