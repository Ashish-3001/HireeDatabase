# Generated by Django 3.0.5 on 2020-06-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0003_auto_20200610_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='eyee_type_hotel',
            field=models.CharField(max_length=80),
        ),
    ]
