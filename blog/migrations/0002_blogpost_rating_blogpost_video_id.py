# Generated by Django 4.1 on 2024-10-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='video_id',
            field=models.CharField(blank=True, default='', max_length=201, null=True),
        ),
    ]
