# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('user_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('study_name', models.CharField(max_length=50)),
                ('user_group', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('questionnaire_id', models.CharField(max_length=50, blank=True)),
                ('started', models.IntegerField(null=True, blank=True)),
                ('finished', models.IntegerField(null=True, blank=True)),
                ('progress_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'progress',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questionnaires',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('role', models.CharField(max_length=50)),
                ('study_name', models.CharField(max_length=50)),
                ('user_group', models.CharField(max_length=50)),
                ('questionnaire_id', models.CharField(max_length=50)),
                ('questionnaire_name', models.CharField(max_length=50)),
                ('save_as', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'questionnaires',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('questionnaire_id', models.CharField(max_length=45)),
                ('var_id', models.CharField(max_length=45, blank=True)),
                ('var_name', models.CharField(max_length=100)),
                ('var_value', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('user_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('password_hash', models.TextField(blank=True)),
                ('salt', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='results',
            name='user_id',
            field=models.ForeignKey(to='questionnaire.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='progress',
            name='user_id',
            field=models.ForeignKey(to='questionnaire.Users'),
            preserve_default=True,
        ),
    ]
