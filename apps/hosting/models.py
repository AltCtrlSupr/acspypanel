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
        used_resource =json.loads(self.used_resource)
        if not resource in used_resource: used_resource[resource] = 0
        used_resource[resource] = used_resource[resource] + 1
        self.used_resource = json.dumps(used_resource)
        self.save()

    def used_resource_del(self, resource):
        used_resource =json.loads(self.used_resource)
        if not resource in used_resource: used_resource[resource] = 0
        used_resource[resource] = used_resource[resource] + 1
        self.used_resource = json.dumps(used_resource)
        self.save()

    def get_resources(self):
        resources = {}
        for plan in HostingPlan.objects.filter(hosting=self):
            for r in PlanResource.objects.filter(plan=plan.plan):
                if r.resource.name not in resources: resources[r.resource.name] = { 'label' : r.resource.description, 'value' : r.value }
                else: resources[r.resource.name]['value'] = r.value + resources[r.resource.name]['value'] 
        return ', '.join('%s x %s' % (resources[key]['label'], resources[key]['value']) for key in resources.keys())

    def get_used_resources(self):
        resources = []
        used_resource = json.loads(self.used_resource)
        for r, used in used_resource.iteritems():
            rsc = Resource.objects.get(name=r)
            resources.append('%s x %s' % (rsc.description, used))
        return ', '.join(resources)


    def get_plans(self):
        plans = {}
        for plan in HostingPlan.objects.filter(hosting=self):
            if plan.plan.name not in plans: plans[plan.plan.name] = 1
            else: plans[plan.plan.name] = plans[plan.plan.name] + 1

        return ', '.join('%s x %s' % (plan, count) for (plan, count) in plans.items())

    def get_max_resource(self, resource):
        resources = 0
        print vars(resource)
        for plan in HostingPlan.objects.filter(hosting=self):
            for r in PlanResource.objects.filter(plan=plan.plan, resource=resource):
                resources = resources + r.value
        return resources

    def get_used_resource(self, resource):
        used_resource = json.loads(self.used_resource)
        if resource.name in used_resource: return used_resource[resource.name]
        else: return 0

    def has_available_resource(self, resource):
        max_resource = self.get_max_resource(resource)
        used_resource = self.get_used_resource(resource)

        print "%s < %s" % (used_resource, max_resource)

        if used_resource < max_resource: return True
        else: return False

    @staticmethod
    def find_by_obj(obj):
        if hasattr(obj, 'hosting'):
            return obj.hosting
        else:
            for fk in [ 'domain', 'database', 'dns_domain', 'httpd_host', 'maildomain', 'account'  ]:
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
