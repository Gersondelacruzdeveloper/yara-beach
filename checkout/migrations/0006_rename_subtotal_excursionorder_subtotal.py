# Generated by Django 4.1 on 2022-10-16 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_rename_excurion_name_excursionorder_excursion_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excursionorder',
            old_name='subTotal',
            new_name='subtotal',
        ),
    ]
