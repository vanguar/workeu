# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workeu', '0004_auto_20170514_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(verbose_name='фотография', blank=True, default='', upload_to='static/media/photos'),
        ),
    ]
