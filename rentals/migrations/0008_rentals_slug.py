# Generated by Django 4.1 on 2023-12-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_rentals_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentals',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
