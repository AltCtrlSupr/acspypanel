from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class ACSModelBase(models.Model):
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    permission = GenericRelation('ACSPermission')

    def get_users(self):
        return ', '.join(user.username for user in self.permission.all()[0].user.all())

    class Meta:
        abstract = True

class ACSPermission(models.Model):
    user = models.ManyToManyField(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self): return u'%s -> %s' % (self.content_type, self.content_object)

    def get_users(self): return u', '.join(user.username for user in self.user.all())
