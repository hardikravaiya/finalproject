# Generated by Django 4.1.7 on 2023-03-30 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0007_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 30, 14, 13, 3, 36759)),
        ),
    ]
