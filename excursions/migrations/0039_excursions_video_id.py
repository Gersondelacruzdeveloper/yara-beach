# Generated by Django 4.1 on 2023-11-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0038_excurasion_category_excursions_company_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursions',
            name='video_id',
            field=models.TextField(blank=True, default='', max_length=201, null=True),
        ),
    ]
