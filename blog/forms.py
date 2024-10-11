from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'featured_image', 'keywords', 'meta_description', 'og_title', 'og_description', 'og_image', 'schema_markup', 'is_published']
