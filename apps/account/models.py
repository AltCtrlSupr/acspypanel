from django.db import models
from ..common.models import ACSModelBase, ACSModelUser
from ..domain.models import Domain

class Account(ACSModelUser):
    domain = models.ForeignKey(Domain)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s@%s' % (self.username, self.domain)
