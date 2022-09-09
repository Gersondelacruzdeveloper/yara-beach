# Generated by Django 4.1 on 2022-09-08 19:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0010_remove_excursions_images_excursionsfotos_excursion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExcursionsFotos',
            new_name='ExcursionExtraPhotos',
        ),
        migrations.RenameField(
            model_name='excursions',
            old_name='image_alt',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='excursions',
            old_name='image',
            new_name='main_image',
        ),
        migrations.AlterField(
            model_name='excursions',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
