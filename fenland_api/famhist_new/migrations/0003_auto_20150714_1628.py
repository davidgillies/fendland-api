# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('famhist_new', '0002_auto_20150714_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='famhistquestionnaire',
            options={'verbose_name': 'Family History Questionnaire', 'verbose_name_plural': 'Family History Questionnaires'},
        ),
        migrations.AddField(
            model_name='famhistquestionnaire',
            name='finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='famhistquestionnaire',
            name='user',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
