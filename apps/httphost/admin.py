from django.contrib import admin
from .models import HttpHost, HttpSecureDir
from ..common.admin import ACSModelAdmin

class HttpSecureDirInline(admin.TabularInline):
    model = HttpSecureDir
    extra = 0
    fieldsets = (
            (None, {
                'fields' : [ 'protected_dir', 'users', 'enabled' ]
                }),
            )

class HttpHostAdmin(ACSModelAdmin):
    inlines = [ HttpSecureDirInline, ]
    list_display = [ 'domain', 'php', 'usessl', 'get_users', 'enabled' ]
    fieldsets = (
            (None, {
                'fields': [ 'domain', 'php', 'service' ]
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

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [ 'domain' ]
        return []

    def get_form(self, request, obj=None, **kwargs):
        form = super(HttpHostAdmin, self).get_form(request, obj,**kwargs)
        if request.user.is_superuser and obj == None:
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.exclude(id__in=[httphost.domain.id for httphost in HttpHost.objects.all()])
        else:
            if obj == None:
                form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.exclude(id__in=[httphost.domain.id for httphost in HttpHost.objects.filter(user=request.user)])
        return form

admin.site.register(HttpHost, HttpHostAdmin)
