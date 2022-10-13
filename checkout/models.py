from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


# Creates a Excursion model containing data about each individual Excursion
class ExcursionOrder(models.Model):
    excurion_name = models.CharField(max_length=201, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, blank=False, editable=False)
    Full_name = models.CharField(max_length=70, null=False, blank=False)
    image = models.URLField(null=True, blank=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    adult_qty =  models.IntegerField(null=False, blank=False)
    child_qty =  models.IntegerField(null=False, blank=False)
    excursion_date = models.DateField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

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
