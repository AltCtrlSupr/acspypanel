from django.contrib import admin
from django.forms.models import ModelForm
from .models import Domain
from ..common.admin import ACSModelAdmin

# Wizard form inlines
from ..httphost.models import HttpHost
from ..maildomain.models import MailDomain
from ..dnsdomain.models import DnsDomain

class DomainAdmin(ACSModelAdmin):
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'hosting', 'parent_domain', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'user', 'enabled' )
                }),
            )
    list_display = [ 'domain', 'parent_domain', 'hosting', 'is_httpd_alias', 'is_dns_alias', 'is_mail_alias', 'get_users', 'enabled' ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(DomainAdmin, self).get_form(request, obj,**kwargs)
        form.base_fields['parent_domain'].queryset = form.base_fields['parent_domain'].queryset.filter(parent_domain=None)
        return form

class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        return True

class DomainWizard(Domain):
    class Meta:
        proxy = True

class DnsDomainInline(admin.StackedInline):
    model = DnsDomain
    form = AlwaysChangedModelForm
    extra = 0
    fieldsets = (
            (None, {
                'fields': ( 'domain', 'type', 'dyn', 'user' )
                }),
            ('Slave options', {
                'classes': ('collapse',),
                'fields': [ 'master' ]
                }),
            )


class HttpHostInline(admin.StackedInline):
    model = HttpHost
    form = AlwaysChangedModelForm
    extra = 0
    fieldsets = (
            (None, {
                'fields': [ 'enabled', 'php' ]
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



class MailDomainInline(admin.StackedInline):
    model = MailDomain
    form = AlwaysChangedModelForm
    extra = 0
    fieldsets = (
            (None, {
                'fields' : [ 'domain', 'enabled' ]
                }),
            ('Limits', {
                'fields' : [ ( 'max_aliases', 'max_mailboxes', 'max_quota' ) ]
                }),
            )


class DomainWizardAdmin(DomainAdmin):
    inlines = [ HttpHostInline, MailDomainInline, DnsDomainInline ]

admin.site.register(DomainWizard, DomainWizardAdmin)
admin.site.register(Domain, DomainAdmin)
