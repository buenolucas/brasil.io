# Generated by Django 2.2 on 2020-04-15 19:13

import covid19.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0005_auto_20200414_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statespreadsheet',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=covid19.models.default_data_json),
        ),
    ]