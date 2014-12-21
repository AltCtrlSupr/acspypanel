# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20141221_1509'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logrcvd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=255)),
                ('goto', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maildir', models.CharField(max_length=255)),
                ('quota_limit', models.BigIntegerField(default=100)),
                ('used_quota', models.BigIntegerField(default=0)),
                ('bytes', models.BigIntegerField(default=0)),
                ('messages', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
                ('max_aliases', models.IntegerField()),
                ('max_mailboxes', models.IntegerField()),
                ('max_quota', models.BigIntegerField()),
                ('backupmx', models.BooleanField(default=False)),
                ('domain', models.OneToOneField(to='domain.Domain')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WBList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender', models.CharField(max_length=64)),
                ('reject', models.CharField(max_length=200, blank=True)),
                ('blacklisted', models.BooleanField(default=False)),
                ('rcpt', models.ForeignKey(to='maildomain.Mailbox')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mailbox',
            name='domain',
            field=models.ForeignKey(to='maildomain.MailDomain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailbox',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailbox',
            name='username',
            field=models.OneToOneField(to='account.Account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailalias',
            name='domain',
            field=models.ForeignKey(to='maildomain.MailDomain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailalias',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logrcvd',
            name='rcpt',
            field=models.ForeignKey(to='maildomain.Mailbox'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logrcvd',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
