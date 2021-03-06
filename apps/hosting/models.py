from django.db import models
from ..common.models import ACSModelBase, ACSPermission
from ..account.models import Account
from django.contrib.contenttypes.models import ContentType
import json
from django.contrib.auth.models import User, Permission

class Hosting(ACSModelBase):
    owner = models.ForeignKey(Account, related_name = 'hosting_owner')
    name = models.CharField(max_length=200)
    plan = models.ManyToManyField('Plan', through='HostingPlan')
    resource = models.ManyToManyField('Resource', through='HostingResource')

    def used_resource_add(self, resource):
        rsc = HostingResource.objects.get(hosting=self, resource=resource)
        rsc.count = rsc.count + 1
        rsc.save()

    def used_resource_del(self, resource):
        rsc = HostingResource.objects.get(hosting=self, resource=resource)
        rsc.count = rsc.count - 1
        rsc.save()
        
    def get_resources(self):
        resources = {}
        for plan in HostingPlan.objects.filter(hosting=self):
            for r in PlanResource.objects.filter(plan=plan.plan):
                if r.resource.name not in resources: resources[r.resource.name] = { 'label' : r.resource.description, 'value' : 0 }
                resources[r.resource.name]['value'] = r.value if type(r.value) == long else 0 + resources[r.resource.name]['value'] 
        return ', '.join('%s x %s' % (resources[key]['label'], resources[key]['value']) for key in resources.keys())

    def get_used_resources(self):
        return ', '.join('%s x %s' % (hr.resource.description, hr.count) for hr in HostingResource.objects.filter(hosting=self))

    def get_plans(self):
        plans = {}
        for plan in HostingPlan.objects.filter(hosting=self):
            if plan.plan.name not in plans: plans[plan.plan.name] = 1
            else: plans[plan.plan.name] = plans[plan.plan.name] + 1

        return ', '.join('%s x %s' % (plan, count) for (plan, count) in plans.items())

    def get_max_resource(self, resource):
        resources = 0
        for plan in HostingPlan.objects.filter(hosting=self):
            for r in PlanResource.objects.filter(plan=plan.plan, resource=resource):
                resources = resources + r.value if type(r.value) == long else 0
        return resources

    def get_used_resource(self, resource):
        try:
            return HostingResource.objects.get(hosting=self, resource=resource).count
        except:
            return None

    def has_available_resource(self, resource):
        max_resource = self.get_max_resource(resource)
        used_resource = self.get_used_resource(resource)

        if used_resource is None: return False
        if used_resource <= max_resource: return True
        return False

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

# Workaround to find only valid content types, children of ACSModelBase, change this in future to ACSModelBaseResource or something
class ContentTypeManager(models.Manager):
    def resource_models(self, test = None):
        ct = []
        for c in ContentType.objects.all():
            if c.model_class()().__class__.__bases__[0].__name__ == 'ACSModelBase':
                ct.append(c)
        return ct

class Resource(ACSModelBase):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    default = models.IntegerField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    objects = ContentTypeManager()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='parent_resource')

    def __unicode__(self): return u'%s' % self.name

    class Meta:
        unique_together = ( 'name', 'content_type' )

class Plan(ACSModelBase):
    name = models.CharField(max_length=50)
    resources = models.ManyToManyField(Resource, through='PlanResource')

    def __unicode__(self): return u'%s' % self.name

    def save(self, *args, **kwargs):
        super(Plan, self).save(*args, **kwargs)
        for hp in Hosting.objects.filter(plan=self):
            hp.save()

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
        for r in self.plan.resources.all():
            (hr, created) = HostingResource.objects.get_or_create(resource = r, hosting=self.hosting)
            for perm in Permission.objects.filter(content_type=r.content_type):
                self.hosting.owner.adminuser.user_permissions.add(perm)
        self.hosting.owner.adminuser.save()

class HostingResource(ACSModelBase):
    resource = models.ForeignKey(Resource)
    hosting = models.ForeignKey(Hosting)
    count = models.PositiveIntegerField(default=0)

    def __unicode__(self): u'%s x %s' % (self.resource.description, self.count)
