from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from ..common.models import ACSModelBase

class SettingKey(models.Model):
    TYPES = (
        ( 'string', 'String' ),
        ( 'check', 'Check Box' ),
        ( 'int', 'Integer' ),
        ( 'model', 'Model' ),
    )
    key = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    required = models.BooleanField(default=False)
    type = models.CharField(max_length=10, choices=TYPES, default='string')
    string_value = models.CharField(max_length=255, null=True, blank=True)
    int_value = models.IntegerField(null=True, blank=True)
    bool_value = models.NullBooleanField(null=True, blank=True)
    scope = models.ForeignKey(ContentType)

    def __unicode__(self): return u'%s' % self.label

    def save(self, *args, **kwargs):
        super(SettingKey, self).save(*args, **kwargs)
        # Create and update default values for all objects
        for obj in ContentType.get_all_objects_for_this_type(self.scope):
            (sv, created) = SettingValue.objects.get_or_create(key=self, scope=ContentType.objects.get_for_model(obj), object_id=obj.pk)
            if not created:
                sv.save()



class SettingValue(ACSModelBase):
    key = models.ForeignKey(SettingKey)
    string_value = models.CharField(max_length=255, null=True, blank=True)
    int_value = models.IntegerField(null=True, blank=True)
    bool_value = models.NullBooleanField(null=True, blank=True)
    use_default = models.BooleanField(default=True)

    scope = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('scope', 'object_id')

    def get_value(self):
        if hasattr(self, '%s_value' % self.key.type):
            return u'%s' % getattr(self, '%s_value' % self.key.type)
        return u'%s' % self.string_value


    def save(self, *args, **kwargs):
        if self.use_default:
            self.string_value = self.key.string_value
            self.int_value = self.key.int_value
            self.bool_value = self.key.bool_value
        super(SettingValue, self).save(*args, **kwargs)
