# Generated by Django 3.0.3 on 2020-06-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0008_remove_workday_total_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='workday',
            name='total_time',
            field=models.TextField(default=None, null=True),
        ),
    ]