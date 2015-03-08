from django.contrib import admin
from .models import Account
from ..common.admin import ACSModelAdmin


class AccountAdmin(ACSModelAdmin):
    fieldsets = (
            (None, {
                'fields': ( ('username', 'domain'), 'password', 'enabled', 'user' )
                }),
            )

    list_display = [ 'username', 'domain', 'enabled' ]


admin.site.register(Account, AccountAdmin)
