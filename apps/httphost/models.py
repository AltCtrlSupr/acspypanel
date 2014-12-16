from django.db import models
from ..common.models import ACSModelBase
from ..domain.models import Domain
from ..account.models import Account

class HttpHost(ACSModelBase):
    domain = models.ForeignKey(Domain, unique=True)
#    service = models.ForeignKey('Service', blank=True, null=True)
    configuration = models.TextField(blank=True)
    php = models.BooleanField(default=False)
#    proxy_service = models.ForeignKey('Service', blank=True, null=True)
    usessl = models.BooleanField(default=False)
    certificate = models.TextField(blank=True)
    certificate_key = models.TextField(blank=True)
    certificate_chain = models.TextField(blank=True)
    certificate_authority = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.domain

    def save(self, *args, **kwargs):
        super(HttpHost, self).save(*args, **kwargs)

class HttpLocation(ACSModelBase):
    httpd_host = models.ForeignKey(HttpHost)
    protected_dir = models.CharField(max_length=255)
    users = models.ManyToManyField(Account)
    
    def __unicode__(self):
        return u'%s' % self.protected_dir
