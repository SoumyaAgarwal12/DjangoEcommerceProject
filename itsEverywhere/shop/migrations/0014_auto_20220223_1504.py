# Generated by Django 3.1.1 on 2022-02-23 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20220223_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 15, 4, 50, 11270)),
        ),
    ]
