from django.db import models
from ..common.models import ACSModelBase
from ..account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Hosting(ACSModelBase):
    owner = models.ForeignKey(Account, related_name = 'hosting_owner')
    name = models.CharField(max_length=200)
    plan = models.ManyToManyField('Plan', through='HostingPlan')

    def get_resources(self):
        resources = {}
        for plan in HostingPlan.objects.filter(user=self):
            for r in PlanResource.objects.filter(plan=plan.plan):
                if r.resource.name not in resources: resources[r.resource.name] = { 'label' : r.resource.description, 'value' : r.value }
                else: resources[r.resource.name]['value'] = r.value + resources[r.resource.name]['value'] 
        return ', '.join('%s x %s' % (resources[key]['label'], resources[key]['value']) for key in resources.keys())

    def get_plans(self):
        plans = {}
        for plan in HostingPlan.objects.filter(user=self):
            if plan.plan.name not in plans: plans[plan.plan.name] = 1
            else: plans[plan.plan.name] = plans[plan.plan.name] + 1

        return ', '.join('%s x %s' % (plan, count) for (plan, count) in plans.items())

    def __unicode__(self): return u'%s' % self.name

    class Meta:
        unique_together = ( 'name', )

class Resource(ACSModelBase):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    default = models.IntegerField(blank=True, null=True)

    def __unicode__(self): return u'%s' % self.name

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
