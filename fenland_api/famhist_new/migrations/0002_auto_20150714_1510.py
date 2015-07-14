# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('famhist_new', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH04_MotherDiabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH05_MotherAge',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH06_FatherDiabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH07_FatherAge',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH08_Sibling01Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH09_Sibling01Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH10_Sibling01Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH11_Sibling02Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH12_Sibling02Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH13_Sibling02Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH14_Sibling03Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH15_Sibling03Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH16_Sibling03Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH17_Sibling04Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH18_Sibling04Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH19_Sibling04Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH20_Sibling05Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH21_Sibling05Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH22_Sibling05Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH23_Sibling06Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH24_Sibling06Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH25_Sibling06Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH26_Sibling07Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH27_Sibling07Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH28_Sibling07Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH29_Sibling08Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH30_Sibling08Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH31_Sibling08Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH32_Sibling09Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH33_Sibling09Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH34_Sibling09Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH35_Sibling10Type',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'None'), (1, b'Sister'), (2, b'Brother'), (3, b'Half sister'), (4, b'Half Brother')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH36_Sibling10Diabetic',
            field=models.IntegerField(blank=True, null=True, choices=[(-1, b'Please select...'), (2, b'Yes'), (3, b'No'), (4, b'Not known')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='famhistquestionnaire',
            name='FH37_Sibling10Age',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'>10'), (2, b'10-19'), (3, b'20-29'), (4, b'30-39'), (5, b'40-49'), (6, b'50-59'), (7, b'60-69'), (8, b'70+'), (9, b'Not known')]),
            preserve_default=True,
        ),
    ]
