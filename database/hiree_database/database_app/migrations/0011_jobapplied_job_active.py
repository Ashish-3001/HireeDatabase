# Generated by Django 3.0.5 on 2020-06-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0010_joboffer_job_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplied',
            name='job_active',
            field=models.BooleanField(default=True),
        ),
    ]
