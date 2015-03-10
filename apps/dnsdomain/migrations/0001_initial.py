# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('type', models.CharField(max_length=6, choices=[(b'MASTER', b'Master'), (b'SLAVE', b'Slave')])),
                ('notified_serial', models.IntegerField(null=True, blank=True)),
                ('account', models.CharField(max_length=40, blank=True)),
                ('dyn', models.BooleanField(default=False)),
                ('soa', models.IntegerField(default=1)),
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
                ('type', models.CharField(max_length=6, choices=[(b'A', b'A'), (b'CNAME', b'CNAME'), (b'MX', b'MX'), (b'NS', b'NS'), (b'PTR', b'PTR'), (b'SOA', b'SOA'), (b'SRV', b'SRV'), (b'TXT', b'TXT')])),
                ('content', models.CharField(max_length=255, blank=True)),
                ('ttl', models.IntegerField(null=True, blank=True)),
                ('prio', models.IntegerField(null=True, blank=True)),
                ('dns_domain', models.ForeignKey(to='dnsdomain.DnsDomain')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
