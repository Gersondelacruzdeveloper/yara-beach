from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

# Excursion model
class Excursions(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=201, null=True)
    image = models.ImageField(upload_to='images/excursions/uploads/', null=True)
    description = RichTextUploadingField(null=True, blank=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
