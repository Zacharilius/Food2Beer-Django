# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food2beer_app', '0004_auto_20150323_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('beer', models.ManyToManyField(to='food2beer_app.Beer')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='brewery',
            options={'ordering': ['name'], 'verbose_name_plural': 'Breweries'},
        ),
    ]
