# Generated by Django 3.0.5 on 2020-06-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0004_auto_20200610_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='job_posted_dasignation',
            new_name='job_posted_designation',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='job_posted_name',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_posted_by',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
