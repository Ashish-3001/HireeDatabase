# Generated by Django 3.0.5 on 2020-06-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0008_jobapplied_joboffer_shortlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_no_emplyee_offered',
            field=models.IntegerField(default=0),
        ),
    ]