# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamHistQuestionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FH03_BrotherTotal', models.IntegerField(null=True, blank=True)),
                ('FH02_SisterTotal', models.IntegerField(null=True, blank=True)),
                ('FH04_MotherDiabetic', models.NullBooleanField()),
                ('FH05_MotherAge', models.IntegerField(null=True, blank=True)),
                ('FH06_FatherDiabetic', models.NullBooleanField()),
                ('FH07_FatherAge', models.IntegerField(null=True, blank=True)),
                ('FH08_Sibling01Type', models.IntegerField(null=True, blank=True)),
                ('FH09_Sibling01Diabetic', models.NullBooleanField()),
                ('FH10_Sibling01Age', models.IntegerField(null=True, blank=True)),
                ('FH11_Sibling02Type', models.IntegerField(null=True, blank=True)),
                ('FH12_Sibling02Diabetic', models.NullBooleanField()),
                ('FH13_Sibling02Age', models.IntegerField(null=True, blank=True)),
                ('FH14_Sibling03Type', models.IntegerField(null=True, blank=True)),
                ('FH15_Sibling03Diabetic', models.NullBooleanField()),
                ('FH16_Sibling03Age', models.IntegerField(null=True, blank=True)),
                ('FH17_Sibling04Type', models.IntegerField(null=True, blank=True)),
                ('FH18_Sibling04Diabetic', models.NullBooleanField()),
                ('FH19_Sibling04Age', models.IntegerField(null=True, blank=True)),
                ('FH20_Sibling05Type', models.IntegerField(null=True, blank=True)),
                ('FH21_Sibling05Diabetic', models.NullBooleanField()),
                ('FH22_Sibling05Age', models.IntegerField(null=True, blank=True)),
                ('FH23_Sibling06Type', models.IntegerField(null=True, blank=True)),
                ('FH24_Sibling06Diabetic', models.NullBooleanField()),
                ('FH25_Sibling06Age', models.IntegerField(null=True, blank=True)),
                ('FH26_Sibling07Type', models.IntegerField(null=True, blank=True)),
                ('FH27_Sibling07Diabetic', models.NullBooleanField()),
                ('FH28_Sibling07Age', models.IntegerField(null=True, blank=True)),
                ('FH29_Sibling08Type', models.IntegerField(null=True, blank=True)),
                ('FH30_Sibling08Diabetic', models.NullBooleanField()),
                ('FH31_Sibling08Age', models.IntegerField(null=True, blank=True)),
                ('FH32_Sibling09Type', models.IntegerField(null=True, blank=True)),
                ('FH33_Sibling09Diabetic', models.NullBooleanField()),
                ('FH34_Sibling09Age', models.IntegerField(null=True, blank=True)),
                ('FH35_Sibling10Type', models.IntegerField(null=True, blank=True)),
                ('FH36_Sibling10Diabetic', models.NullBooleanField()),
                ('FH37_Sibling10Age', models.IntegerField(null=True, blank=True)),
                ('FH38_FamilyHistoryEntryComments', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
