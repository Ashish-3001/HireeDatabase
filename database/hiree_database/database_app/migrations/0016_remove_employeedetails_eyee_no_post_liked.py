# Generated by Django 3.0.5 on 2020-06-21 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0015_auto_20200618_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='eyee_no_post_liked',
        ),
    ]
