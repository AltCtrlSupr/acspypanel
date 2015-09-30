from django.db import models
from ..common.models import ACSModelBase
#from ..hosting.models import Hosting

class Domain(ACSModelBase):
    domain = models.CharField(unique=True, max_length=255)
    hosting = models.ForeignKey('hosting.Hosting')
    parent_domain = models.ForeignKey('self', blank=True, null=True, related_name= 'parent_domain_rel')
    is_httpd_alias = models.BooleanField(default=False)
    is_dns_alias = models.BooleanField(default=False)
    is_mail_alias = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.domain

    class Meta:
        unique_together = ( 'domain', )
