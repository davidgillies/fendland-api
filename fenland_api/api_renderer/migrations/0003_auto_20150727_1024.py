# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_renderer', '0002_auto_20150727_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='surgery',
            name='latitude',
            field=models.FloatField(help_text='Latitude (Lat.) is the angle between any point and the equator (north pole is at 90; south pole is at -90).', null=True, verbose_name='latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='surgery',
            name='longitude',
            field=models.FloatField(help_text='Longitude (Long.) is the angle east or west of an arbitrary point on Earth from Greenwich (UK), which is the international zero-longitude point (longitude=0 degrees). The anti-meridian of Greenwich is both 180 (direction to east) and -180 (direction to west).', null=True, verbose_name='longitude', blank=True),
            preserve_default=True,
        ),
    ]
