from django.db import models
from ..common.models import ACSModelBase
from ..account.models import Account

class IpAddress(ACSModelBase):
    ip = models.CharField(max_length=39)
    netmask = models.CharField(max_length=39)
    gateway = models.CharField(max_length=39, blank=True, null=True)
    iface = models.CharField(max_length=20, blank=True, null=True)
    alias = models.BooleanField(default=False)

    def __unicode__(self): return u'%s' % self.ip

class Server(ACSModelBase):
    hostname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ip = models.ManyToManyField(IpAddress)
    uid_base = models.IntegerField(default=1000)
    gid_base = models.IntegerField(default=1000)
    home_base = models.CharField(max_length=255, default='/home')

    def __unicode__(self): return u'%s' % self.hostname

class ServiceType(ACSModelBase):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True)
    
    def __unicode__(self): return u'%s' % self.name

class Service(ACSModelBase):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ServiceType)
    server = models.ForeignKey(Server)
    ip = models.ForeignKey(IpAddress)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
        for ci in ConfigItem.objects.filter(servicetype=self.type):
            ConfigValue.objects.get_or_create(service=self, setting_key=ci, value=ci.default_value)

    def __unicode__(self): return u'%s' % self.name

class ConfigItem(ACSModelBase):
    TYPES = (
            ( 'string', 'String' ),
            ( 'check', 'Check Box' ),
            ( 'int', 'Integer' ),
            )
    key = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPES)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    required = models.BooleanField(default=False)
    servicetype = models.ForeignKey(ServiceType)

    def __unicode__(self): return u'%s' % self.label


class ConfigValue(ACSModelBase):
    service = models.ForeignKey(Service)
    setting_key = models.ForeignKey(ConfigItem)
    value = models.TextField()

    def __unicode__(self): return u'%s' % self.setting_key.label
