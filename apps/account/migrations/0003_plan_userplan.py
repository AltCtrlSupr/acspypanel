# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20141221_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plan_name', models.CharField(max_length=50)),
                ('max_panel_reseller', models.IntegerField(null=True, blank=True)),
                ('max_panel_user', models.IntegerField(null=True, blank=True)),
                ('max_httpd_host', models.IntegerField(null=True, blank=True)),
                ('max_httpd_alias', models.IntegerField(null=True, blank=True)),
                ('max_httpd_user', models.IntegerField(null=True, blank=True)),
                ('max_dns_domain', models.IntegerField(null=True, blank=True)),
                ('max_mail_domain', models.IntegerField(null=True, blank=True)),
                ('max_mail_mailbox', models.IntegerField(null=True, blank=True)),
                ('max_mail_alias', models.IntegerField(null=True, blank=True)),
                ('max_mail_alias_domain', models.IntegerField(null=True, blank=True)),
                ('max_ftpd_user', models.IntegerField(null=True, blank=True)),
                ('max_domain', models.IntegerField(null=True, blank=True)),
                ('max_db', models.IntegerField(null=True, blank=True)),
                ('max_db_user', models.IntegerField(null=True, blank=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('puser', models.ForeignKey(related_name='puser', to='account.Account')),
                ('uplan', models.ForeignKey(related_name='uplan', to='account.Plan')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
