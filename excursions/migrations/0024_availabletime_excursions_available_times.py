# Generated by Django 4.1 on 2023-08-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0023_reference_email_reference_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='excursions',
            name='available_times',
            field=models.ManyToManyField(to='excursions.availabletime'),
        ),
    ]