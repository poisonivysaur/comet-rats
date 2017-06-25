# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rats', '0006_remove_residency_duration_in_mins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='residency',
            name='duration_in_mins',
            field=models.IntegerField(default=90),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='attendance',
            name='residency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rats.Residency'),
        ),
    ]
