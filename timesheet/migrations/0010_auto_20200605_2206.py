# Generated by Django 3.0.3 on 2020-06-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0009_workday_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='total_time',
            field=models.FloatField(default=None, null=True),
        ),
    ]