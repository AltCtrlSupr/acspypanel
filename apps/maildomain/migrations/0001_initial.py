# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domain', '0001_initial'),
        ('account', '0001_initial'),
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
                ('rcpt', models.CharField(max_length=64)),
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
                ('quota_limit', models.BigIntegerField()),
                ('used_quota', models.BigIntegerField()),
                ('bytes', models.BigIntegerField()),
                ('messages', models.IntegerField()),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('rcpt', models.CharField(max_length=64)),
                ('reject', models.CharField(max_length=200, blank=True)),
                ('blacklisted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
            model_name='logrcvd',
            name='mail_domain',
            field=models.ForeignKey(to='maildomain.MailDomain'),
            preserve_default=True,
        ),
    ]
