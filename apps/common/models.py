from django.db import models
from django.contrib.auth.models import User


class ACSModelBase(models.Model):
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ACSModelUser(ACSModelBase):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True
