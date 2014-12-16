from django.db import models
from ..common.models import ACSModelBase
from ..domain.models import Domain

class DnsDomain(ACSModelBase):
    TYPES=(
            ('MASTER', 'Master'),
            ('SLAVE', 'Slave'),
            )
    domain = models.ForeignKey(Domain, unique=True)
#    service = models.ForeignKey('Service', blank=True, null=True)
    master = models.CharField(max_length=20, blank=True)
    last_check = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=6,choices=TYPES)
    notified_serial = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True)
    soa = models.IntegerField(default=1)

    def __unicode__(self):
        return u'%s' % self.domain

    def save(self, createSOA=False, *args, **kwargs):
        if not self.id: createSOA=True
        super(DnsDomain, self).save(createSOA, *args, **kwargs)
        if createSOA:
            self.create_soa()

    def create_soa(self):
        soa = DnsRecord()
        soa.dns_domain = self
        soa.name = self.domain.domain
        soa.type='SOA'
        soa.content=u'%s ns@%s %d' % (self.domain.domain, self.domain.domain, self.soa)
        soa.ttl = 3600
        soa.save()

    def update_soa(self):
        self.soa = self.soa + 1
        self.save()
        soa = DnsRecord.objects.get(dns_domain=self,type='SOA')
        soa.content=u'%s ns@%s %d' % (self.domain.domain, self.domain.domain, self.soa)
        soa.save()

class DnsRecord(ACSModelBase):
    TYPES=(
            ('A','A'),
            ('CNAME','CNAME'),
            ('MX','MX'),
            ('NS','NS'),
            ('PTR','PTR'),
            ('SOA','SOA'),
            ('SRV','SRV'),
            ('TXT','TXT'),
            )
    dns_domain = models.ForeignKey(DnsDomain)
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=6, choices=TYPES)
    content = models.CharField(max_length=255, blank=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        super(DnsRecord, self).save(*args, **kwargs)
        if self.type != 'SOA':
            self.dns_domain.update_soa()
