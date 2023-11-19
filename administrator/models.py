from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone 
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=201, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    post = RichTextUploadingField(null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)

 

    def __str__(self):
        return self.name
    