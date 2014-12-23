from django.db import models
from ..common.models import ACSModelBase
from ..domain.models import Domain
from ..account.models import Account

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



class MailDomain(ACSModelBase):
    domain = models.OneToOneField(Domain)
    #service = models.ForeignKey('Service', blank=True, null=True)
    max_aliases = models.IntegerField(default=10)
    max_mailboxes = models.IntegerField(default=10)
    max_quota = models.BigIntegerField(default=10)
    backupmx = models.BooleanField(default=False)

class MailAlias(ACSModelBase):
    domain = models.ForeignKey(MailDomain)
    address = models.CharField(max_length=255)
    goto = models.TextField()

class Mailbox(ACSModelBase):
    username = models.OneToOneField(Account)
    domain = models.ForeignKey(MailDomain)
    maildir = models.CharField(max_length=255)
    quota_limit = models.BigIntegerField(default=100)
    used_quota = models.BigIntegerField(default=0)
    bytes = models.BigIntegerField(default=0)
    messages = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.username

    def save(self, *args, **kwargs):
        super(Mailbox, self).save(*args, **kwargs)
        self.username.adminuser.user_permissions.add(Permission.objects.get(content_type=ContentType.objects.get_for_model(Mailbox), codename='change_mailbox'))
        self.username.adminuser.user_permissions.add(Permission.objects.get(content_type=ContentType.objects.get_for_model(WBList), codename='change_wblist'))
        self.username.adminuser.user_permissions.add(Permission.objects.get(content_type=ContentType.objects.get_for_model(WBList), codename='add_wblist'))
        self.username.adminuser.user_permissions.add(Permission.objects.get(content_type=ContentType.objects.get_for_model(WBList), codename='delete_wblist'))

class WBList(ACSModelBase):
    rcpt = models.ForeignKey(Mailbox)
    sender = models.CharField(max_length=64)
    reject = models.CharField(max_length=200, blank=True)
    blacklisted = models.BooleanField(default=False)

class Logrcvd(ACSModelBase):
    rcpt = models.ForeignKey(Mailbox)
    sender = models.CharField(max_length=64)
