# Generated by Django 4.1 on 2022-09-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0006_alter_excursions_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursions',
            name='alt',
            field=models.CharField(blank=True, max_length=201, null=True),
        ),
    ]
