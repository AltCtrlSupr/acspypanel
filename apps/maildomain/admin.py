from django.contrib import admin
from ..common.admin import ACSModelAdmin
from .models import MailDomain, Mailbox, MailAlias, WBList, Logrcvd
from ..account.models import Account



class MailboxInline(admin.TabularInline):
    model = Mailbox
    extra = 1
    fieldsets = (
            (None, {
                'fields': [ 'username', 'quota_limit', 'enabled' ]
                }),
            )

    def formfield_for_foreignkey(self, field, request, **kwargs):
        maildomain = self.get_object(request, MailDomain)
        queryset = None
        if field.name == "username":
            kwargs["queryset"] = Account.objects.filter(domain=maildomain.domain)#.exclude(id__in=[mailbox.username.id for mailbox in Mailbox.objects.filter(domain=maildomain)])
            print request
        return super(MailboxInline, self).formfield_for_foreignkey(field, request, **kwargs)

    def get_object(self, request, model):
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-1]
        return model.objects.get(pk=object_id)

class MailAliasInline(admin.TabularInline):
    model = MailAlias
    extra = 0

class MailDomainAdmin(ACSModelAdmin):
    inlines = [ MailboxInline, MailAliasInline ]
    list_display = [ 'domain', 'max_aliases', 'max_mailboxes', 'max_quota', 'enabled', 'user' ]
    fieldsets = (
            (None, {
                'fields' : [ 'domain', 'user', 'enabled' ]
                }),
            ('Limits', {
                'fields' : [ ( 'max_aliases', 'max_mailboxes', 'max_quota' ) ]
                }),
            )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [ 'domain' ]
        return []

    def get_form(self, request, obj=None, **kwargs):
        form = super(MailDomainAdmin, self).get_form(request, obj,**kwargs)
        if request.user.is_superuser and obj == None:
            form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.exclude(id__in=[maildomain.domain.id for maildomain in MailDomain.objects.all()])
        else:
            if obj == None:
               form.base_fields['domain'].queryset = form.base_fields['domain'].queryset.filter(user=request.user).exclude(id__in=[maildomain.domain.id for maildomain in MailDomain.objects.filter(user=request.user)]) 
        return form


admin.site.register(MailDomain, MailDomainAdmin)
