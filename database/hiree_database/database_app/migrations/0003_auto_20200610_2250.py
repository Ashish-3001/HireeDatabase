# Generated by Django 3.0.5 on 2020-06-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0002_auto_20200609_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='eyee_phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employerdetails',
            name='eyer_phone',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
