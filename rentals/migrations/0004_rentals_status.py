# Generated by Django 4.1 on 2022-09-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_alter_rentals_accom_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentals',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20),
        ),
    ]
