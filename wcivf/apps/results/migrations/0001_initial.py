# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-07 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elections', '0016_postelection_contested'),
        ('people', '0024_personpost_elected'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_declaration_time', models.DateTimeField(blank=True)),
                ('declaration_time', models.DateTimeField(blank=True)),
                ('person_posts', models.ManyToManyField(to='people.PersonPost')),
                ('post_election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.PostElection')),
            ],
        ),
    ]
