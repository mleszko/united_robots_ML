# Generated by Django 4.0.4 on 2022-04-18 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_robots', '0003_alter_position_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 19, 8, 30, 219868)),
        ),
    ]