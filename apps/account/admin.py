from django.contrib import admin
from .models import Account, Plan, UserPlan
from ..common.admin import ACSModelAdmin


class UserPlanInline(admin.TabularInline):
    model = UserPlan
    extra = 1
    fieldsets = (
            (None, {
                'fields': [ 'uplan' ]
                }),
            )

class AccountAdmin(ACSModelAdmin):
    inlines = [ UserPlanInline, ]
    fieldsets = (
            (None, {
                'fields': ( ('username', 'domain'), 'password', 'enabled', 'user' )
                }),
            )

    list_display = [ 'username', 'domain', 'enabled', 'get_plans', 'get_max_httpd_host' ]

admin.site.register(Account, AccountAdmin)
admin.site.register(Plan)
