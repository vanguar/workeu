# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workeu', '0005_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='postf',
            name='photo',
            field=models.ImageField(upload_to='static/media/photos', verbose_name='фотография', blank=True, default=''),
        ),
        migrations.AddField(
            model_name='postp',
            name='photo',
            field=models.ImageField(upload_to='static/media/photos', verbose_name='фотография', blank=True, default=''),
        ),
    ]
