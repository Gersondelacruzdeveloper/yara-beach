# Generated by Django 4.1 on 2023-12-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentals',
            name='meta_description',
            field=models.CharField(blank=True, default='', max_length=201, null=True),
        ),
    ]
