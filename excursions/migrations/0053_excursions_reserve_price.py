# Generated by Django 4.1 on 2024-01-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0052_alter_excursions_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursions',
            name='reserve_price',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=7),
        ),
    ]
