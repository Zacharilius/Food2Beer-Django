# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food2beer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brewery',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='brewery',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 3, 23, 3, 1, 53, 479411, tzinfo=utc), unique=True, max_length=40),
            preserve_default=False,
        ),
    ]
