# Generated by Django 4.1 on 2023-12-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_excursionorder_where_heard_from_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursionorder',
            name='url_flight',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]