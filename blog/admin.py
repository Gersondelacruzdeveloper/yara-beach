from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogImage
admin.site.register(BlogPost)
admin.site.register(BlogImage)



