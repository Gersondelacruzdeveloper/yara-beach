# Generated by Django 4.1 on 2022-09-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0002_remove_excursions_images_excursions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursions',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/excursions/uploads/'),
        ),
    ]
