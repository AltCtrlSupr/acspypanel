from django.db import models
from ..common.models import ACSModelBase
from ..domain.models import Domain
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Account(ACSModelBase):
    adminuser = models.OneToOneField(User,related_name='adminuser',blank=True)
    domain = models.ForeignKey(Domain, blank=True, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    hosting = models.ForeignKey('hosting.Hosting', blank=True, null=True)
    is_hosting_owner = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.adminuser.username

    def save(self, *args, **kwargs):
        # Create or update django user
        if self.domain:
            (user, created) = User.objects.get_or_create(username='@'.join([self.username, self.domain.domain]))
        else:
            (user, created) = User.objects.get_or_create(username=self.username)
        if not created:
            origin = Account.objects.get(pk=self.pk)
            if self.password != origin.password:
                user.set_password(self.password)
        else:
            user.set_password(self.password)
        user.is_staff = True
        user.save()

        user.user_permissions.add(Permission.objects.get(content_type=ContentType.objects.get_for_model(Account), codename='change_account'))

        # Defining account
        self.adminuser = user
        super(Account, self).save(*args, **kwargs)
