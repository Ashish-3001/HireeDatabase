# Generated by Django 3.0.5 on 2020-06-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0005_auto_20200611_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_working_days',
            field=models.CharField(max_length=10),
        ),
    ]
