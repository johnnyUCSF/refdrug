# Generated by Django 3.0.3 on 2020-06-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
            ],
        ),
    ]
