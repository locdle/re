# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0002_auto_20150501_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('rating', models.BooleanField(default=False)),
                ('question_response', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='rating',
            name='starq',
        ),
        migrations.DeleteModel(
            name='Textq',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Starq',
        ),
    ]
