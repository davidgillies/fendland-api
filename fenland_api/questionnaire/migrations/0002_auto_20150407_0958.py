# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'User Progress', 'verbose_name_plural': 'User Progress'},
        ),
        migrations.AlterModelOptions(
            name='questionnaires',
            options={'verbose_name': 'Questionnaire', 'verbose_name_plural': 'Questionnaires'},
        ),
        migrations.AlterModelOptions(
            name='results',
            options={'verbose_name': 'User Result', 'verbose_name_plural': 'User Results'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='user_id',
            new_name='user',
        ),
    ]
