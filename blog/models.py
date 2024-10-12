from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    video_id = models.CharField(null=True, blank=True, max_length=201, default='')
    rating = models.IntegerField(null=True, blank=True, default=0)
    # SEO and Social Media Fields
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    og_title = models.CharField(max_length=255, blank=True, null=True)  # Open Graph Title
    og_description = models.CharField(max_length=300, blank=True, null=True)  # Open Graph Description
    og_image = models.ImageField(upload_to='blog_og_images/', blank=True, null=True)  # Open Graph Image
    schema_markup = models.TextField(blank=True, null=True)  # Custom JSON-LD Schema


    # Performance fields
    view_count = models.IntegerField(default=0)  # To track views
    read_time = models.IntegerField(default=0)  # Estimated reading time in minutes

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'

    def get_meta_title(self):
        return self.og_title if self.og_title else self.title

    def get_meta_description(self):
        return self.meta_description if self.meta_description else self.content[:150]

    def generate_schema_markup(self):
        # Basic schema.org structure for Article type
        schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": self.title,
            "author": {
                "@type": "Person",
                "name": self.author.get_full_name(),
            },
            "datePublished": self.created_at.strftime('%Y-%m-%d'),
            "image": self.featured_image.url if self.featured_image else '',
            "publisher": {
                "@type": "Organization",
                "name": "Punta Cana Discovery",
                "logo": {
                    "@type": "ImageObject",
                    "url": "/static/images/excursions/Logo.png"  # Update this with actual logo path
                }
            },
            "description": self.get_meta_description(),
        }
        return schema

    def update_read_time(self):
        # Simple reading time calculation (assumes 200 words per minute)
        word_count = len(self.content.split())
        self.read_time = word_count // 200
        self.save()


class BlogImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()  # Stores the image URL
