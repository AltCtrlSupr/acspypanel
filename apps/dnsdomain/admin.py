from django.contrib import admin
from .models import DnsDomain, DnsRecord
from .forms import DnsRecordInlineForm
from ..common.admin import ACSModelAdmin

class DnsRecordInline(admin.TabularInline):
    model = DnsRecord
    extra = 0
    fieldsets = (
            (None, {
                'fields': [ 'name', 'type', 'content', 'ttl', 'prio', 'enabled', 'user' ]
                }),
            )
    form = DnsRecordInlineForm

class DnsDomainAdmin(ACSModelAdmin):
    inlines = [ DnsRecordInline, ]
    list_display = [ 'domain', 'type', 'get_users', 'dyn', 'enabled' ]
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'type', 'dyn', 'user' )
                }),
            ('Slave options', {
                'classes': ('collapse',),
                'fields': [ 'master' ]
                }),
            )

    def save_model(self, request, obj, form, change):
        super(DnsDomainAdmin, self).save_model(request, obj, form, change)
        obj.save()


class DnsRecordAdmin(ACSModelAdmin):
    list_display = [ 'name' ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [ 'dns_domain', 'name' ]
        return []

    def get_form(self, request, obj=None, **kwargs):
        form = super(DnsRecordAdmin, self).get_form(request, obj,**kwargs)
        if not request.user.is_superuser and obj == None:
            form.base_fields['dns_domain'].queryset = form.base_fields['dns_domain'].queryset.filter(user=request.user) | form.base_fields['dns_domain'].queryset.filter(dyn=True)

        return form


admin.site.register(DnsDomain, DnsDomainAdmin)
admin.site.register(DnsRecord, DnsRecordAdmin)
