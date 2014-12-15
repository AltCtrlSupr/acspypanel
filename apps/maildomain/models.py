from django.db import models
from ..common.models import ACSModelBase, ACSModelUser
from ..domain.models import Domain
from ..account.models import Account


class MailDomain(ACSModelUser):
    domain = models.OneToOneField(Domain)
    #service = models.ForeignKey('Service', blank=True, null=True)
    description = models.CharField(max_length=255)
    max_aliases = models.IntegerField()
    max_mailboxes = models.IntegerField()
    max_quota = models.BigIntegerField()
    backupmx = models.BooleanField(default=False)

class MailAlias(ACSModelBase):
    domain = models.ForeignKey(MailDomain)
    address = models.CharField(max_length=255)
    goto = models.TextField()

class Mailbox(ACSModelBase):
    username = models.OneToOneField(Account)
    domain = models.ForeignKey(MailDomain)
    maildir = models.CharField(max_length=255)
    quota_limit = models.BigIntegerField()
    used_quota = models.BigIntegerField(default=0)
    bytes = models.BigIntegerField(default=0)
    messages = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.username

class WBList(ACSModelUser):
    sender = models.CharField(max_length=64)
    rcpt = models.CharField(max_length=64)
    reject = models.CharField(max_length=200, blank=True)
    blacklisted = models.BooleanField(default=False)

class Logrcvd(ACSModelBase):
    sender = models.CharField(max_length=64)
    rcpt = models.CharField(max_length=64)
    mail_domain = models.ForeignKey(MailDomain)
