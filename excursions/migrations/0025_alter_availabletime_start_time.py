# Generated by Django 4.1 on 2023-08-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0024_availabletime_excursions_available_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='start_time',
            field=models.TimeField(),
        ),
    ]