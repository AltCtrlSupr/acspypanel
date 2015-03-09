from django import forms

from .models import Mailbox

class MailboxInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MailboxInlineForm, self).__init__(*args, **kwargs)
        # fix this
#        if self.instance.pk:
#            self.fields['username'].widget.attrs['readonly'] = 'True'
#            self.fields['username'].widget.attrs['disabled'] = 'disabled'


    class Meta:
        model = Mailbox
        fields = '__all__'

