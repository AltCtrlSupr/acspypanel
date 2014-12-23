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

class IpAddress(models.Model):
    user = models.ForeignKey(FosUser, blank=True, null=True)
    ip = models.CharField(max_length=39)
    enabled = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_address'


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
