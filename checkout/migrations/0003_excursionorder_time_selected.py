# Generated by Django 4.1 on 2023-08-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_excursionorder_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursionorder',
            name='time_selected',
            field=models.CharField(default='', max_length=200),
        ),
    ]
