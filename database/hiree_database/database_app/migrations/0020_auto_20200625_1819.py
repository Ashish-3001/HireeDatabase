# Generated by Django 3.0.5 on 2020-06-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0019_joboffer_short_listed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='eyee_aadhar_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='eyee_address_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='eyee_address_2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='eyee_name',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='eyee_place_pre_experience',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='employerdetails',
            name='eyer_address_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employerdetails',
            name='eyer_address_2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employerdetails',
            name='eyer_gst_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employerdetails',
            name='eyer_hotel_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='eyer_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_experience',
            field=models.CharField(max_length=40),
        ),
    ]
