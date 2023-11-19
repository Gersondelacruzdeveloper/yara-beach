from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=201, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    post = RichTextUploadingField(null=False, blank=False)
 

    def __str__(self):
        return self.name
    