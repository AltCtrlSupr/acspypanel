# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnsdomain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnsdomain',
            name='soa',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dnsdomain',
            name='type',
            field=models.CharField(max_length=6, choices=[(b'MASTER', b'Master'), (b'SLAVE', b'Slave')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dnsrecord',
            name='type',
            field=models.CharField(max_length=6, choices=[(b'A', b'A'), (b'CNAME', b'CNAME'), (b'MX', b'MX'), (b'NS', b'NS'), (b'PTR', b'PTR'), (b'SOA', b'SOA'), (b'SRV', b'SRV'), (b'TXT', b'TXT')]),
            preserve_default=True,
        ),
    ]
