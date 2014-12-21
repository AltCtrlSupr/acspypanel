from django.db import models
from ..common.models import ACSModelBase
from ..domain.models import Domain
from django.contrib.auth.models import User


class Account(ACSModelBase):
    adminuser = models.OneToOneField(User,related_name='adminuser',blank=True)
    domain = models.ForeignKey(Domain)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s@%s' % (self.username, self.domain)

    def save(self, *args, **kwargs):
        # Create or update django user
        (user, created) = User.objects.get_or_create(username='@'.join([self.username, self.domain.domain]))
        if self.pk:
            origin = Account.objects.get(pk=self.pk)
            if self.password != origin.password:
                user.set_password(self.password)
        else:
            user.set_password(self.password)
        user.is_staff = True
        user.save()

        # Defining account
        self.adminuser = user
        super(Account, self).save(*args, **kwargs)

