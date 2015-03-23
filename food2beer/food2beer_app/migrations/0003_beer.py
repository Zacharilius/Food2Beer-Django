# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food2beer_app', '0002_auto_20150323_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('beerType', models.CharField(max_length=200)),
                ('abv', models.IntegerField()),
                ('ibus', models.IntegerField()),
                ('brewery', models.ForeignKey(to='food2beer_app.Brewery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
