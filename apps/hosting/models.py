from django.db import models
from ..common.models import ACSModelBase
from ..account.models import Account
from django.contrib.contenttypes.models import ContentType
import json

class Hosting(ACSModelBase):
    owner = models.ForeignKey(Account, related_name = 'hosting_owner')
    name = models.CharField(max_length=200)
    plan = models.ManyToManyField('Plan', through='HostingPlan')
    used_resource = models.TextField(default={})

    def used_resource_add(self, resource):
        self.used_resource[resource] = self.used_resource[resource] + 1

    def used_resource_del(self, resource):
        self.used_resource[resource] = self.used_resource[resource] - 1

    def get_resources(self):
        resources = {}
        for plan in HostingPlan.objects.filter(hosting=self):
            for r in PlanResource.objects.filter(plan=plan.plan):
                if r.resource.name not in resources: resources[r.resource.name] = { 'label' : r.resource.description, 'value' : r.value }
                else: resources[r.resource.name]['value'] = r.value + resources[r.resource.name]['value'] 
        return ', '.join('%s x %s' % (resources[key]['label'], resources[key]['value']) for key in resources.keys())

    def get_plans(self):
        plans = {}
        for plan in HostingPlan.objects.filter(hosting=self):
            if plan.plan.name not in plans: plans[plan.plan.name] = 1
            else: plans[plan.plan.name] = plans[plan.plan.name] + 1

        return ', '.join('%s x %s' % (plan, count) for (plan, count) in plans.items())

    def get_resource_from_contenttype(self, content_type):
        resources = 0
        for plan in HostingPlan.objects.filter(hosting=self):
            for r in PlanResource.objects.filter(plan=plan.plan, resource=Resource.object.get(content_type=content_type)):
                resources = resources + r.value
        return resources

    @staticmethod
    def find_by_obj(obj):
        if hasattr(obj, 'hosting'):
            return obj.hosting
        else:
            for fk in [ 'domain', 'database', 'dns_domain', 'httpd_host', 'maildomain'  ]:
                if hasattr(obj, fk):
                    fk_obj = getattr(obj, fk, None)
                    if not isinstance(fk_obj, unicode) and fk_obj is not None:
                        find = Hosting.find_by_obj(fk_obj)
                        if find is not False: return find
        return False



    def __unicode__(self): return u'%s' % self.name

    class Meta:
        unique_together = ( 'name', )

class Resource(ACSModelBase):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    default = models.IntegerField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType)

    def __unicode__(self): return u'%s' % self.name

    class Meta:
        unique_together = ( 'name', 'content_type' )

class Plan(ACSModelBase):
    name = models.CharField(max_length=50)
    resources = models.ManyToManyField(Resource, through='PlanResource')

    def __unicode__(self): return u'%s' % self.name

class PlanResource(ACSModelBase):
    resource = models.ForeignKey(Resource)
    plan = models.ForeignKey(Plan)
    value = models.IntegerField(blank=True, null=True)

    def __unicode__(self): return u'%s' % self.resource.name

class HostingPlan(ACSModelBase):
    plan = models.ForeignKey(Plan)
    hosting = models.ForeignKey(Hosting)

    def __unicode__(self): return u'%s' % self.plan.name

    def save(self, *args, **kwargs):
        super(HostingPlan, self).save(*args, **kwargs)
        used_resource = json.loads(self.hosting.used_resource)
        for r in self.plan.resources.all():
            if r.name not in used_resource: used_resource[r.name] = 0

        self.hosting.used_resource = json.dumps(used_resource)
        self.hosting.save()
