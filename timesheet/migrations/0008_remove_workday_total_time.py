# Generated by Django 3.0.3 on 2020-06-05 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0007_auto_20200605_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workday',
            name='total_time',
        ),
    ]