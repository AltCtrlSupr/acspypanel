from __future__ import unicode_literals
from django.db import models


class ConfigSetting(models.Model):
    user = models.ForeignKey('FosUser', blank=True, null=True)
    server = models.ForeignKey('Server', blank=True, null=True)
    service = models.ForeignKey('Service', blank=True, null=True)
    setting_key = models.CharField(max_length=255)
    value = models.TextField()
    context = models.CharField(max_length=255)
    focus = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_setting'


class DatabaseUser(models.Model):
    database = models.ForeignKey('Db', blank=True, null=True)
    username = models.CharField(max_length=16)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'database_user'


class Db(models.Model):
    service = models.ForeignKey('Service', blank=True, null=True)
    user = models.ForeignKey('FosUser', blank=True, null=True)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        managed = False
        db_table = 'db'


class FieldType(models.Model):
    setting_key = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'field_type'


class FosGroup(models.Model):
    name = models.CharField(unique=True, max_length=255)
    roles = models.TextField()

    class Meta:
        managed = False
        db_table = 'fos_group'


class FosUser(models.Model):
    parent_user = models.ForeignKey('self', blank=True, null=True)
    username = models.CharField(max_length=255)
    username_canonical = models.CharField(unique=True, max_length=255)
    email = models.CharField(max_length=255)
    email_canonical = models.CharField(unique=True, max_length=255)
    enabled = models.IntegerField()
    salt = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)
    locked = models.IntegerField()
    expired = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=255, blank=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)
    roles = models.TextField()
    credentials_expired = models.IntegerField()
    credentials_expire_at = models.DateTimeField(blank=True, null=True)
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    uid = models.IntegerField(blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    password_changed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fos_user'


class FosUserUserGroup(models.Model):
    goup = models.ForeignKey(FosUser)
    user = models.ForeignKey(FosGroup)

    class Meta:
        managed = False
        db_table = 'fos_user_user_group'


class FtpdUser(models.Model):
    user = models.ForeignKey(FosUser, blank=True, null=True)
    service = models.ForeignKey('Service', blank=True, null=True)
    user_name = models.CharField(max_length=16)
    password = models.CharField(max_length=255)
    uid = models.IntegerField()
    gid = models.IntegerField()
    dir = models.CharField(max_length=255)
    quota = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ftpd_user'


class HttpdHost(models.Model):
    domain = models.ForeignKey(Domain, unique=True, blank=True, null=True)
    service = models.ForeignKey('Service', blank=True, null=True)
    configuration = models.TextField(blank=True)
    cgi = models.IntegerField(blank=True, null=True)
    ssi = models.IntegerField(blank=True, null=True)
    php = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    proxy_service = models.ForeignKey('Service', blank=True, null=True)
    usessl = models.IntegerField(blank=True, null=True)
    certificate = models.TextField(blank=True)
    certificate_key = models.TextField(blank=True)
    certificate_chain = models.TextField(blank=True)
    certificate_authority = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'httpd_host'


class HttpdUser(models.Model):
    httpd_host = models.ForeignKey(HttpdHost, blank=True, null=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    protected_dir = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'httpd_user'


class IpAddress(models.Model):
    user = models.ForeignKey(FosUser, blank=True, null=True)
    ip = models.CharField(max_length=39)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_address'


class MailAlias(models.Model):
    mail_domain = models.ForeignKey('MailDomain', blank=True, null=True)
    address = models.CharField(max_length=255)
    goto = models.TextField()
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailDomain(models.Model):
    domain = models.ForeignKey(Domain, unique=True, blank=True, null=True)
    user = models.ForeignKey(FosUser, blank=True, null=True)
    service = models.ForeignKey('Service', blank=True, null=True)
    description = models.CharField(max_length=255)
    max_aliases = models.IntegerField()
    max_mailboxes = models.IntegerField()
    max_quota = models.BigIntegerField()
    backupmx = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_domain'


class MailLogrcvd(models.Model):
    sender = models.CharField(max_length=64)
    rcpt = models.CharField(max_length=64)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    mail_domain = models.ForeignKey(MailDomain, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_logrcvd'


class MailMailbox(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    maildir = models.CharField(max_length=255)
    quota_limit = models.BigIntegerField()
    used_quota = models.BigIntegerField()
    bytes = models.BigIntegerField()
    messages = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    mail_domain = models.ForeignKey(MailDomain, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mailbox'


class MailWblist(models.Model):
    user = models.ForeignKey(FosUser, blank=True, null=True)
    sender = models.CharField(max_length=64)
    rcpt = models.CharField(max_length=64)
    reject = models.CharField(max_length=200, blank=True)
    blacklisted = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wblist'


class Plan(models.Model):
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
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    max_domain = models.IntegerField(blank=True, null=True)
    max_db = models.IntegerField(blank=True, null=True)
    max_db_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class Server(models.Model):
    user = models.ForeignKey(FosUser, blank=True, null=True)
    ip = models.ForeignKey(IpAddress, blank=True, null=True)
    hostname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server'


class Service(models.Model):
    user = models.ForeignKey(FosUser, blank=True, null=True)
    server = models.ForeignKey(Server, blank=True, null=True)
    type = models.ForeignKey('ServiceType', blank=True, null=True)
    ip = models.ForeignKey(IpAddress, blank=True, null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceType(models.Model):
    parent_type = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'service_type'


class ServicetypeFieldtype(models.Model):
    servicetype = models.ForeignKey(ServiceType)
    fieldtype = models.ForeignKey(FieldType)

    class Meta:
        managed = False
        db_table = 'servicetype_fieldtype'


class UserPlan(models.Model):
    uplans = models.ForeignKey(Plan, blank=True, null=True)
    puser = models.ForeignKey(FosUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_plan'


class WpSetup(models.Model):
    httpd_host = models.ForeignKey(HttpdHost, unique=True, blank=True, null=True)
    database_user = models.ForeignKey(DatabaseUser, blank=True, null=True)
    user = models.ForeignKey(FosUser, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_setup'
