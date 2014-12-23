from django.db import models
from ..common.models import ACSModelBase
from ..account.models import Account


class FtpdUser(ACSModelBase):
    username = models.OneToOneField(Account)
    uid = models.IntegerField(blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    dir = models.CharField(max_length=255, default='/')
    quota = models.IntegerField(blank=True, null=True)
