from django.contrib import admin
from .models import DnsDomain, DnsRecord

#class DomainAdmin(admin.ModelAdmin):
#    list_display = [ 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias' ]
#    fieldsets = (
#            (None, {
#                'fields': ( 'domain', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'user', 'enabled' )
#                }),
#            )

class DnsRecordInline(admin.TabularInline):
    model = DnsRecord
    extra = 0
    fieldsets = (
            (None, {
                'fields': [ 'name', 'type', 'content', 'ttl', 'prio', 'enabled' ]
                }),
            )

class DnsDomainAdmin(admin.ModelAdmin):
    inlines = [ DnsRecordInline, ]
    list_display = [ 'domain', 'type', 'master' ]
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'type' )
                }),
            ('Slave options', {
                'classes': ('collapse',),
                'fields': [ 'master' ]
                }),
            )
    def queryset(self, request):
        qs = super(DnsDomainAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(DnsDomain, DnsDomainAdmin)
admin.site.register(DnsRecord)
