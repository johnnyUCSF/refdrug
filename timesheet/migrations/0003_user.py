# Generated by Django 3.0.3 on 2020-06-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0002_auto_20200603_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.IntegerField(unique=True)),
                ('first_name', models.TextField(max_length=30)),
                ('last_name', models.TextField(max_length=30)),
            ],
        ),
    ]
