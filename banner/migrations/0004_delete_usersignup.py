# Generated by Django 4.1.7 on 2023-03-28 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_alter_usersignup_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userSignup',
        ),
    ]
