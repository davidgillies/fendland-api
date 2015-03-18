# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('repeat', models.IntegerField(null=True, blank=True)),
                ('studyphase', models.IntegerField(null=True, blank=True)),
                ('appt_date', models.DateField(null=True, blank=True)),
                ('appt_time', models.TimeField(null=True, blank=True)),
                ('test_site', models.CharField(max_length=10, blank=True)),
                ('modified_by', models.CharField(max_length=45, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'appointments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('reason', models.TextField(blank=True)),
                ('edit_date', models.DateField(null=True, blank=True)),
                ('editor', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'audit_log',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('curr_status', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'status',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=50, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('addr1', models.CharField(max_length=50, blank=True)),
                ('addr2', models.CharField(max_length=50, blank=True)),
                ('town', models.CharField(max_length=50, blank=True)),
                ('county', models.CharField(max_length=50, blank=True)),
                ('postcode', models.CharField(max_length=50, blank=True)),
                ('telephone', models.CharField(max_length=12, blank=True)),
                ('admin_contact_name', models.CharField(max_length=50, blank=True)),
                ('admin_contact_number', models.CharField(max_length=50, blank=True)),
                ('hscic_code', models.CharField(max_length=45, blank=True)),
                ('area', models.CharField(max_length=50, blank=True)),
                ('modified_by', models.CharField(max_length=50, db_column=b'modified by', blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('surgeriescol', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'surgeries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.IntegerField(serialize=False, primary_key=True)),
                ('surname', models.CharField(max_length=50, blank=True)),
                ('forenames', models.CharField(max_length=50, blank=True)),
                ('initials', models.CharField(max_length=10, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('title', models.CharField(max_length=10, blank=True)),
                ('sex', models.CharField(max_length=1, blank=True)),
                ('addr1', models.CharField(max_length=50, blank=True)),
                ('addr2', models.CharField(max_length=50, blank=True)),
                ('town', models.CharField(max_length=50, blank=True)),
                ('county', models.CharField(max_length=50, blank=True)),
                ('postcode', models.CharField(max_length=50, blank=True)),
                ('home_tel', models.CharField(max_length=50, blank=True)),
                ('work_tel', models.CharField(max_length=50, blank=True)),
                ('mobile', models.CharField(max_length=50, blank=True)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('nhs_no', models.CharField(max_length=10, blank=True)),
                ('surgery_id', models.IntegerField(null=True, blank=True)),
                ('gp_id', models.IntegerField(null=True, blank=True)),
                ('moved_away', models.IntegerField(null=True, blank=True)),
                ('diabetes_diagnosed', models.IntegerField(null=True, blank=True)),
                ('modified_by', models.CharField(max_length=50, blank=True)),
                ('curr_status', models.IntegerField(null=True, blank=True)),
                ('reason', models.IntegerField(null=True, blank=True)),
                ('phase1_comment', models.TextField(blank=True)),
                ('phase2_comment', models.TextField(blank=True)),
                ('volunteerscol', models.CharField(max_length=45, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('surgeries', models.ForeignKey(to='api_renderer.Surgery')),
            ],
            options={
                'db_table': 'volunteers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appointment',
            name='volunteer',
            field=models.ForeignKey(to='api_renderer.Volunteer'),
            preserve_default=True,
        ),
    ]
