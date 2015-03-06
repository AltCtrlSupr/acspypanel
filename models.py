from __future__ import unicode_literals
from django.db import models

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
