from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone 
from django.utils.text import slugify
from django.core.exceptions import ValidationError
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=201, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    post = RichTextUploadingField(null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # If the slug is not provided, generate it based on the name
        if not self.slug:
            self.slug = slugify(self.name)

        # Ensure the slug is unique
        if Post.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError('Slug already exists. Please provide a unique name.')

        super().save(*args, **kwargs)
