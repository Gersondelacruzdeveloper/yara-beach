# Generated by Django 4.1 on 2023-09-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0026_alter_availabletime_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='bank_acount_type',
            field=models.CharField(choices=[('cc', 'Cuenta corriente '), ('ca', 'Cuenta de ahorro')], default='cuenta corriente ', max_length=20),
        ),
    ]