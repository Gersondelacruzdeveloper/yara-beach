# Generated by Django 4.1 on 2022-09-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0003_alter_excursions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursions',
            name='image',
            field=models.ImageField(null=True, upload_to='excursions/uploads/'),
        ),
    ]
