from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import random
import string


# Create your models here.

# Creates a Excursion model containing data about each individual Excursion
class Excursions(models.Model):
    CHOICES = (
       ('Active', ('Active')),
       ('Inactive', ('Inactive')),
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=201, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, default=0)
    main_image = models.ImageField(upload_to='excursions/uploads/', null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)
    description = RichTextUploadingField(null=False, blank=False, default='')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=CHOICES, default='Inactive', max_length=20)

    def __str__(self):
        return self.title
    

# Creates all the Excursion fotos
class Photos(models.Model):
    excursion = models.ForeignKey(Excursions, null=True, blank=True, on_delete=models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='excursions/uploads/', null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)
    
    def __str__(self):
        return self.image_name


# Creates excursion review model 
class Review(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True,)
    content = models.TextField(null=True, blank=True,)
    rating = models.IntegerField(null=True, blank=True, default=0)
    excursion = models.ForeignKey(Excursions, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Reference(models.Model):
    CHOICES = (
       ('CC', ('Cuenta corriente ')),
       ('CA', ('Cuenta de ahorro')),
    )

    """
    A model representing a reference for a bank account.
    """
    full_name = models.CharField(max_length=255, blank=True, null=True, help_text="The full name of the account holder.")
    bank_name = models.CharField(max_length=255, blank=True, null=True, help_text="The name of the bank.")
    reference_number = models.CharField(max_length=6, unique=True, blank=True, null=True, help_text="The unique 6-digit reference number.")
    account_number = models.CharField(max_length=255, blank=True, null=True, help_text="The bank account number.")
    cedula = models.CharField(max_length=30, blank=True, null=True, help_text="Cedula")
    bank_acount_type = models.CharField(choices=CHOICES, default='cuenta corriente ', max_length=20)
    created = models.DateField(auto_now_add=True, help_text="The date when the reference was created.")

    def __str__(self):
        return self.reference_number

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_unique_reference_number()
        super(Reference, self).save(*args, **kwargs)

    def generate_unique_reference_number(self):
        # Generate a random 6-digit alphanumeric reference number
        length = 6
        characters = string.ascii_letters + string.digits
        reference_number = ''.join(random.choice(characters) for _ in range(length))

        # Check if the generated reference number is unique, if not regenerate until it's unique
        while Reference.objects.filter(reference_number=reference_number).exists():
            reference_number = ''.join(random.choice(characters) for _ in range(length))

        return reference_number




