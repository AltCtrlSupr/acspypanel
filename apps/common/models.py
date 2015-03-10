from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission
from django.core.exceptions import ValidationError


class ACSModelBase(models.Model):
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    permission = GenericRelation('ACSPermission')

    def get_users(self):
        return ', '.join(user.username for user in self.permission.all()[0].user.all())

    def save(self, *args, **kwargs):
        from ..hosting.models import Hosting, Resource
        hosting = Hosting.find_by_obj(self)
        if hosting:
            model = ContentType.objects.get_for_model(self)
            try:
                resource = Resource.objects.get(content_type=model)
            except:
                resource = None
            unlimited_resources = [ 'hostingplan', 'hostingresource' ]
            if model.model not in unlimited_resources:
                if resource:
                    if not hosting.has_available_resource(resource):
                        raise ValidationError('User no has enough resources for %s' % model.model)
                else: 
                    raise ValidationError('This resource is unavailable: %s' % model.model)
            if not self.pk and resource is not None:
                hosting.used_resource_add(resource)
        super(ACSModelBase, self).save(*args, **kwargs)

    def get_hosting(self):
        try:
            from ..hosting.models import Hosting, Resource
            return Hosting.find_by_obj(self)
        except:
            return None

    get_hosting.short_description = 'hosting'

    class Meta:
        abstract = True

class ACSPermission(models.Model):
    user = models.ManyToManyField(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self): return u'%s -> %s' % (self.content_type, self.content_object)

    def get_users(self): return u', '.join(user.username for user in self.user.all())

    def save(self, *args, **kwargs):
        super(ACSPermission, self).save(*args, **kwargs)
        for user in self.user.all():
            for p in Permission.objects.filter(content_type=ContentType.objects.get_for_model(self.content_object)):
                user.user_permissions.add(p)
