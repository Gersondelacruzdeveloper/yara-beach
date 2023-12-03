from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
import random
import string
from decimal import Decimal
# New slug field
from django.utils.text import slugify
from django.db.models import Count
from django.utils import timezone  # Import timezone module
from django.core.exceptions import ValidationError



# Create your models here.
class AvailableTime(models.Model):
    start_time = models.CharField(max_length=201, null=True, blank=True)

    def __str__(self):
        return self.start_time
    
class DayOfWeek(models.Model):
    day_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.day_number)

# Create your models here.
class Excurasion_category(models.Model):
    category = models.CharField(max_length=201, null=True, blank=True)

    def __str__(self):
        return self.category
    
    # Create your models here.
class Excursion_type(models.Model):
    category = models.CharField(max_length=201, null=True, blank=True)

    def __str__(self):
        return self.category
    

# Creates a Excursion model containing data about each individual Excursion
class Excursions(models.Model):
    CHOICES = (
        ('Active', ('Active')),
        ('Inactive', ('Inactive')),
    )
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=201, null=True)
    Price = models.DecimalField(

        max_digits=7, decimal_places=2, null=False, blank=False, default=0)
    main_image = models.ImageField(upload_to='excursions/uploads/',  blank=True, null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)
    description = RichTextUploadingField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(
        choices=CHOICES, default='Inactive', max_length=20)
    is_transfer = models.BooleanField(default=False)  # Boolean field for transfer
    available_times = models.ManyToManyField(AvailableTime)
    unavailable_days = models.ManyToManyField('DayOfWeek', related_name='excursions', blank=True, null=True)
    duration_time = models.IntegerField(null=True, blank=True, default=0)
    tour_guide = models.BooleanField(default=False)  # Boolean field for transfer
    transportation = models.BooleanField(default=False)  # Boolean field for transfer
    slugy = models.SlugField(unique=True, blank=True)
    group =  models.BooleanField(default=False)  # Boolean field for group
    category = models.ManyToManyField('Excurasion_category', related_name='Excurasion_category', blank=True, null=True)
    type_dropdown = models.ManyToManyField('Excursion_type', related_name='Excursion_type', blank=True, null=True)
    company_Price = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False, default=0)
    video_id = models.CharField(null=True, blank=True, max_length=201, default='')
    dicount = models.BooleanField(default=True)  # Boolean field for transfer
    just_adult = models.BooleanField(default=False)  # Boolean field for transfer
    meta_description = models.CharField(max_length=201, null=True, blank=True, default='')
    price_children = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False, default=0)


    def save(self, *args, **kwargs):
        # If the slug is not provided, generate it based on the name
        if not self.slugy:
            self.slugy = slugify(self.title[:50])


        # Ensure the slug is unique
        if Excursions.objects.filter(slugy=self.slugy).exclude(pk=self.pk).exists():
            raise ValidationError('Slug already exists. Please provide a unique name.')
       # Set price_children to half of the Price by default
       
        if self.price_children == 0:
            self.price_children = self.Price / 2

        super().save(*args, **kwargs)
     
    def clean(self):
        super().clean()

        # Check if the description is still the default message
        if self.description == 'Default description message.':
            raise ValidationError({'description': 'Please provide a description.'})



# Creates all the Excursion fotos
class Photos(models.Model):
    excursion = models.ForeignKey(
        Excursions, null=True, blank=True, on_delete=models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='excursions/uploads/', null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)

    def __str__(self):
        return self.image_name


# Creates excursion review model
class Review(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True,)
    content = models.TextField(null=True, blank=True,)
    rating = models.IntegerField(null=True, blank=True, default=0)
    excursion = models.ForeignKey(
        Excursions, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Reference(models.Model):
    CHOICES = (
        ('cc', ('Cuenta corriente ')),
        ('ca', ('Cuenta de ahorro')),
    )

    """
    A model representing a reference for a bank account.
    """
    full_name = models.CharField(
        max_length=255, blank=True, null=True, help_text="The full name of the account holder.")
    bank_name = models.CharField(
        max_length=255, blank=True, null=True, help_text="The name of the bank.")
    reference_number = models.CharField(
        max_length=6, unique=True, blank=True, null=True, help_text="The unique 6-digit reference number.")
    account_number = models.CharField(
        max_length=255, blank=True, null=True, help_text="The bank account number.")
    cedula = models.CharField(
        max_length=30, blank=True, null=True, help_text="Cedula")
    bank_acount_type = models.CharField(
        choices=CHOICES, default='cuenta corriente ', max_length=20)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      help_text="The amount of money that has been paid since the account started.")
    due_to_pay_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, help_text="The amount that needs to be paid after 3 days.")
    has_due_payment = models.BooleanField(
        default=False, help_text="Indicates whether there is a due payment or not.")
    created = models.DateField(
        auto_now_add=True, help_text="The date when the reference was created.")
      # New Fields
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, help_text="Phone number of the account holder.")
    email = models.EmailField(
        max_length=255, blank=True, null=True, help_text="Email address of the account holder.")

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_unique_reference_number()
        super(Reference, self).save(*args, **kwargs)

    def generate_unique_reference_number(self):
        # Generate a random 6-digit alphanumeric reference number
        length = 6
        characters = string.ascii_lowercase + string.digits
        reference_number = ''.join(random.choice(characters)
                                   for _ in range(length))

        # Check if the generated reference number is unique, if not regenerate until it's unique
        while Reference.objects.filter(reference_number=reference_number).exists():
            reference_number = ''.join(random.choice(characters)
                                       for _ in range(length))

        return reference_number


# This to collect the person info in order to sell and add the excursions
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    person_incharge_name = models.CharField(max_length=100, blank=True, null=True)
    prices = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class PageVisit(models.Model):
    page_url = models.CharField(max_length=255)
    visit_datetime = models.DateTimeField(auto_now_add=True)
    visit_count = models.IntegerField(default=0)  # Total visit count

    class Meta:
        permissions = [
            ("can_add_pagevisit", "Can add PageVisit"),
            ("can_change_pagevisit", "Can change PageVisit"),
            ("can_delete_pagevisit", "Can delete PageVisit"),
    ]

    def __str__(self):
        return self.page_url

    def get_absolute_url(self):
        return reverse('page_visit_detail', args=[str(self.id)])



