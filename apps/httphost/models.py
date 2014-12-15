from django.db import models
from ..common.models import ACSModelUser
from ..domain.models import Domain

class HttpHost(ACSModelUser):
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
        if not self.id:
            self.user=self.domain.user
        super(HttpHost, self).save(*args, **kwargs)
