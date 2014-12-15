# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DnsDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('master', models.CharField(max_length=20, blank=True)),
                ('last_check', models.IntegerField(null=True, blank=True)),
                ('type', models.CharField(max_length=6)),
                ('notified_serial', models.IntegerField(null=True, blank=True)),
                ('account', models.CharField(max_length=40, blank=True)),
                ('domain', models.ForeignKey(to='domain.Domain', unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DnsRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(max_length=6)),
                ('content', models.CharField(max_length=255, blank=True)),
                ('ttl', models.IntegerField(null=True, blank=True)),
                ('prio', models.IntegerField(null=True, blank=True)),
                ('dns_domain', models.ForeignKey(to='dnsdomain.DnsDomain')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
