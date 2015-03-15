from django.contrib import admin
from .models import SettingKey, SettingValue
from ..common.admin import ACSModelAdmin

class SettingValueAdmin(ACSModelAdmin):
    list_display = [ 'key', 'get_value' ]

admin.site.register(SettingKey)
admin.site.register(SettingValue, SettingValueAdmin)
