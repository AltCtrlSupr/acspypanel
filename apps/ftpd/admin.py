from django.contrib import admin
from .models import FtpdUser
from ..common.admin import ACSModelAdmin


class FtpdUserAdmin(ACSModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(FtpdUserAdmin, self).get_form(request, obj,**kwargs)
        form.base_fields['username'].queryset = form.base_fields['username'].queryset.exclude(domain__isnull=True)
        return form

admin.site.register(FtpdUser, FtpdUserAdmin)
