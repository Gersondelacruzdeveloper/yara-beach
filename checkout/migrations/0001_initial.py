# Generated by Django 4.1 on 2022-10-20 23:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_name', models.CharField(max_length=300)),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=70)),
                ('image', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('adult_qty', models.IntegerField()),
                ('child_qty', models.IntegerField()),
                ('check_in', models.DateField()),
                ('checkout', models.DateField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cellphone_number', models.CharField(blank=True, max_length=70, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExcursionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excursion_name', models.CharField(max_length=300)),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=70)),
                ('image', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('order_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('adult_qty', models.IntegerField()),
                ('child_qty', models.IntegerField()),
                ('excursion_date', models.DateField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cellphone_number', models.CharField(blank=True, max_length=70, null=True)),
                ('place_pickup', models.CharField(blank=True, max_length=70, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
