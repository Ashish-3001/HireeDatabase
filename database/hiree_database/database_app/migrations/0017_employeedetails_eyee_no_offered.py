# Generated by Django 3.0.5 on 2020-06-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0016_remove_employeedetails_eyee_no_post_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='eyee_no_offered',
            field=models.IntegerField(default=0),
        ),
    ]
