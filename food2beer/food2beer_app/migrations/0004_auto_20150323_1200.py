# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food2beer_app', '0003_beer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='brewery',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='beer',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 3, 23, 12, 0, 58, 807741, tzinfo=utc), unique=True, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
