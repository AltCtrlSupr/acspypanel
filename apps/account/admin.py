from django.contrib import admin
from .models import Account
from ..common.admin import ACSModelAdmin

class AccountAdmin(ACSModelAdmin):
    fieldsets = (
            (None, {
                'fields': ( 'username', 'domain', 'enabled', 'user' )
                }),
            )

    list_display = [ 'username', 'domain', 'enabled', 'user' ]

admin.site.register(Account, AccountAdmin)
