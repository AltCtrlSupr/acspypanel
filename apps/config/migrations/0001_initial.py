# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=10, choices=[(b'string', b'String'), (b'check', b'Check Box'), (b'int', b'Integer')])),
                ('default_value', models.CharField(max_length=255, null=True, blank=True)),
                ('required', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConfigValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=39)),
                ('netmask', models.CharField(max_length=39)),
                ('gateway', models.CharField(max_length=39, null=True, blank=True)),
                ('iface', models.CharField(max_length=20, null=True, blank=True)),
                ('alias', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hostname', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('uid_base', models.IntegerField(default=1000)),
                ('gid_base', models.IntegerField(default=1000)),
                ('home_base', models.CharField(default=b'/home', max_length=255)),
                ('ip', models.ManyToManyField(to='config.IpAddress')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('ip', models.ForeignKey(to='config.IpAddress')),
                ('server', models.ForeignKey(to='config.Server')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, to='config.ServiceType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(to='config.ServiceType'),
        ),
        migrations.AddField(
            model_name='configvalue',
            name='service',
            field=models.ForeignKey(to='config.Service'),
        ),
        migrations.AddField(
            model_name='configvalue',
            name='setting_key',
            field=models.ForeignKey(to='config.ConfigItem'),
        ),
        migrations.AddField(
            model_name='configitem',
            name='servicetype',
            field=models.ForeignKey(to='config.ServiceType'),
        ),
    ]
