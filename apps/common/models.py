from django.db import models
from django.contrib.auth.models import User


class ACSModelBase(models.Model):
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User,blank=True)

    def get_users(self):
        users = []
        for u in self.user.all():
            users.append(u.username)
        return u','.join(users)

    class Meta:
        abstract = True
