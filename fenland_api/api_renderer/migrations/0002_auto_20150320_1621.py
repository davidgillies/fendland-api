# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_renderer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditlog',
            options={'verbose_name': 'Audit Log', 'verbose_name_plural': 'Audit Log'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Status'},
        ),
        migrations.AlterModelOptions(
            name='surgery',
            options={'verbose_name': 'Surgery', 'verbose_name_plural': 'Surgeries'},
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='surgeries',
            field=models.ForeignKey(blank=True, to='api_renderer.Surgery', null=True),
            preserve_default=True,
        ),
    ]
