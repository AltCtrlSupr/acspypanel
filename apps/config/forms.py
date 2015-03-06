from django import forms
from django.core.validators import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin import widgets
from collections import OrderedDict

from .models import ConfigItem


class ConfigItemForm(forms.ModelForm):
    realvalue = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ConfigItemForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            item = self.instance.setting_key

