# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('famhist_new', '0003_auto_20150714_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='famhistquestionnaire',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='famhistquestionnaire',
            name='user',
        ),
    ]
