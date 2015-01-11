from django.db import models
from ..common.models import ACSModelBase
from ..domain.models import Domain
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


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

        user.user_permissions.add(Permission.objects.get(content_type=ContentType.objects.get_for_model(Account), codename='change_account'))

        # Defining account
        self.adminuser = user
        super(Account, self).save(*args, **kwargs)

    def get_max_httpd_host(self):
        count = 0
        data = UserPlan.objects.select_related().filter(puser=self)
        print data.query
        for uplan in data:
            print vars(uplan.uplan)
        for uplan in UserPlan.objects.filter(puser=self):
            if uplan.uplan.max_httpd_host is not None:
                count = count + uplan.uplan.max_httpd_host
        return count

    def get_plans(self):
        plans = []
        for u in UserPlan.objects.filter(puser=self).values('uplan').annotate(models.Sum('uplan')):
            plans.append('Pla: %s x %s' % (Plan.objects.values('plan_name').get(pk=u['uplan'])['plan_name'], u['uplan__sum']))
        return ", \n".join(plans)

class Plan(ACSModelBase):
    plan_name = models.CharField(max_length=50)
    max_panel_reseller = models.IntegerField(blank=True, null=True)
    max_panel_user = models.IntegerField(blank=True, null=True)
    max_httpd_host = models.IntegerField(blank=True, null=True)
    max_httpd_alias = models.IntegerField(blank=True, null=True)
    max_httpd_user = models.IntegerField(blank=True, null=True)
    max_dns_domain = models.IntegerField(blank=True, null=True)
    max_mail_domain = models.IntegerField(blank=True, null=True)
    max_mail_mailbox = models.IntegerField(blank=True, null=True)
    max_mail_alias = models.IntegerField(blank=True, null=True)
    max_mail_alias_domain = models.IntegerField(blank=True, null=True)
    max_ftpd_user = models.IntegerField(blank=True, null=True)
    max_domain = models.IntegerField(blank=True, null=True)
    max_db = models.IntegerField(blank=True, null=True)
    max_db_user = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.plan_name

class UserPlan(ACSModelBase):
    uplan = models.ForeignKey(Plan,related_name='uplan')
    puser = models.ForeignKey(Account,related_name='puser')
