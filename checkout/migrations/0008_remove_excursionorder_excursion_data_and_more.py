# Generated by Django 4.1 on 2023-11-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_excursionorder_excursion_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excursionorder',
            name='Excursion_data',
        ),
        migrations.AddField(
            model_name='excursionorder',
            name='excursion_id',
            field=models.IntegerField(default=None),
        ),
    ]