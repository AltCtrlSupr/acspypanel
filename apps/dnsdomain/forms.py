from django import forms

from .models import DnsDomain, DnsRecord

class DnsRecordInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DnsRecordInlineForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['name'].widget.attrs['readonly'] = 'True'
            self.fields['type'].widget.attrs['disabled'] = 'disabled'


    class Meta:
        model = DnsRecord
        fields = '__all__'

