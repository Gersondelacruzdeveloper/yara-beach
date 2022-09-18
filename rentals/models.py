from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# Creates a Excursion model containing data about each individual Excursion
class Rentals(models.Model):
    CHOICES = (
       ('House', ('Entire House')),
       ('Apartment', ('Entire Aparment')),
       ('Room', ('Single Room')),
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=201, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    main_image = models.ImageField(upload_to='rentals/uploads/', null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    ACCOM_type = models.CharField(choices=CHOICES, default='Room', max_length=20)

    def __str__(self):
        return self.title

    