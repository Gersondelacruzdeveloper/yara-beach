# Generated by Django 4.1 on 2022-10-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursionorder',
            name='cellphone_number',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='excursionorder',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]