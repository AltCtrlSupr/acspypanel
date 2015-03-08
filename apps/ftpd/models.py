from django.db import models
from ..common.models import ACSModelBase
from ..account.models import Account
from ..config.models import Service


class FtpdUser(ACSModelBase):
    username = models.OneToOneField(Account)
    dir = models.CharField(max_length=255, default='/')
    quota = models.IntegerField(blank=True, null=True)
    service = models.ForeignKey(Service)

    def __unicode__(self): return u'%s' % self.username.username
