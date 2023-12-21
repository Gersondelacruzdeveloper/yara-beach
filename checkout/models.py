from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import URLValidator
import uuid
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
# Create your models here.

# Contains all orders related to excursions
class ExcursionOrder(models.Model):
    excursion_name = models.CharField(max_length=300, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, default='')
    order_number = models.CharField(max_length=32, null=False, blank=False, editable=False)
    full_name = models.CharField(max_length=70, null=False, blank=False)
    image = models.TextField(validators=[URLValidator()], null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    adult_qty =  models.IntegerField(null=False, blank=False)
    child_qty =  models.IntegerField(null=False, blank=False)
    infant_qty =  models.IntegerField(null=False, blank=False, default=0)
    excursion_date = models.DateField(null=False, blank=False, default='')
    date_created = models.DateField(auto_now_add=True)
    customer_email = models.EmailField(null=True, blank=True)
    cellphone_number = models.CharField(max_length=70, null=True, blank=True)
    place_pickup = models.CharField(max_length=70, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    reference = models.CharField(max_length=6, null=False, blank=False, default='')
    time_selected = models.CharField(max_length=200, null=False, blank=False, default='')
    excursion_id =  models.IntegerField(null=False, blank=False, default=None)
    advanced = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    remaining = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    where_heard_from_us = models.CharField(max_length=200, null=True, blank=True, default='')

    def _generate_order_number(self):
        """
        Generate a ramdom, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overide the original save method to set the order number
        if it has not been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)


    def __str__(self):
        return self.order_number



# Contains all orders related to rentals
class AccommodationOrder(models.Model):
    rental_name = models.CharField(max_length=300, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, default='')
    order_number = models.CharField(max_length=32, null=False, blank=False, editable=False)
    full_name = models.CharField(max_length=70, null=False, blank=False)
    image = models.TextField(validators=[URLValidator()], null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    adult_qty =  models.IntegerField(null=False, blank=False)
    child_qty =  models.IntegerField(null=False, blank=False)
    check_in = models.DateField(null=False, blank=False)
    checkout = models.DateField(null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    customer_email = models.EmailField(null=True, blank=True)
    cellphone_number = models.CharField(max_length=70, null=True, blank=True)
    rental_type = models.CharField(max_length=70, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_rental_order_number(self):
        """
        Generate a ramdom, unique order number using UUID for rental
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overide the original save method to set the order number
        if it has not been set already
        """
        if not self.order_number:
            self.order_number = self._generate_rental_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number