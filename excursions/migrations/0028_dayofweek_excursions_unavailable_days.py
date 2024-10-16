# Generated by Django 4.1 on 2023-09-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0027_alter_reference_bank_acount_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='excursions',
            name='unavailable_days',
            field=models.ManyToManyField(blank=True, related_name='excursions', to='excursions.dayofweek'),
        ),
    ]
