import schedule
import time
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm  # Assuming you have a BlogPostForm for creating/updating posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import openai
from .models import BlogPost
from datetime import datetime
import random
import string
import random
from django.core.exceptions import ObjectDoesNotExist
from excursions.models import Excursions  # Adjust to your app name
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from openai import OpenAI
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

# BlogPost list view
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'  # Specify your template
    context_object_name = 'posts'
    paginate_by = 10  # Add pagination

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-created_at')


# BlogPost detail view
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'  # Specify your template
    context_object_name = 'post'

    def get_object(self):
        # Increment view count
        post = super().get_object()
        post.view_count += 1
        post.save()
        return post



# Update BlogPost view
class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure the user is the author


# Delete BlogPost view
class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blogpost_list')  # Redirect to blog list

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author




# ----------------------------------------------------create auto blog


def generate_blog_content(excursion_title, excursions_description, excursion_url, duration_time=None, price=None, transportation=None):
    # Create the OpenAI client (make sure to set your API key)
    client = OpenAI(
        api_key= settings.OPENAI_API_KEY # Replace with your actual API key or set it in your environment
    )

    # Create a content prompt for OpenAI with a detailed request for long content
    prompt = f"""
    Write a detailed, SEO-friendly blog post in HTML format about "{excursion_title}" with an optimized, catchy, and SEO-focused title that appeals to travelers in h1. Use the {excursions_description} field to extract location and unique excursion details to make the title and content engaging. However, all information should be uniquely rephrased.

    The blog post should be between 2,100 and 2,400 words. Place all content in the body section, with no header or head tags. Use appropriate HTML tags, paragraphs, and lists. The content should include:
    1. An engaging introduction that captures the reader's interest with keywords like "unforgettable adventure," "top travel experience," and rephrased details from {excursions_description}.
    2. Detailed sections on the main attractions of the excursion, highlighting what makes each stop unique.
    3. Compelling reasons to book this excursion, such as exciting features, scenic views, and immersive experiences.
    4. Personal stories or relatable scenarios to connect with readers, creating a vivid picture of the excursion.
    5. A strong call-to-action with a booking link at the end.
    6. Use keywords related to travel, adventure, and excursions, like "excursion booking," "travel adventure," and rephrased phrases from {excursions_description} to improve search visibility on Google.
    """


    # Append duration if available
    if duration_time:
        prompt += f" Duration: {duration_time}."

    # Append price if available
    if price:
        prompt += f" Price: {price}."

    # Append transportation if available
    if transportation:
        prompt += f" Transportation: {transportation}."

    # Add the additional information
    prompt += (
        " Highlight the main attractions, reasons to book, and add a call-to-action. "
        f"Include this link to the excursion: {excursion_url}."
    )

    # Use the new chat completions API for generating longer text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or use "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes blog posts in HTML format."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3600,  # Limit tokens for content size
        temperature=0.6
    )

    # Extract and return the generated content
    return response.choices[0].message.content



def get_random_excursion():
    # Filter only active excursions
    active_excursions = Excursions.objects.filter(status='Active')
    
    if not active_excursions.exists():
        raise ObjectDoesNotExist("No active excursions available.")
    
    # Choose a random active excursion
    random_excursion = random.choice(active_excursions)
    
    return random_excursion


def get_default_author():
    try:
        # Fetch an existing user (e.g., 'admin' or 'system_user')
        author = User.objects.get(username='Gerson')  # Replace with your default username
    except ObjectDoesNotExist:
        # If the user doesn't exist, create a new one
        author = User.objects.create_user(username='system_user', password='default_password', email='system@domain.com')
        author.is_staff = True  # Make the user an admin/staff if necessary
        author.save()
    return author


def create_blog_post():
    """
    Creates a blog post with a unique, SEO-friendly title and generated content.
    """
    print("creating posts")
    
    excursion = get_random_excursion()
    title = excursion.title
    excursions_description = excursion.description
    duration_time = excursion.duration_time
    price = excursion.price
    transportation = excursion.transportation

    # Generate the blog content
    excursion_url = excursion.get_absolute_url()
    content = generate_blog_content(title, excursions_description, excursion_url, duration_time, price, transportation)
    
    # Parse the HTML to get the H1 title
    soup = BeautifulSoup(content, 'html.parser')
    h1_tag = soup.find('h1')
    title = h1_tag.get_text(strip=True) if h1_tag else title  # Fallback to excursion.title if no <h1> is found
    print('Title:', title)
    print('Content:', content)

    # Get the default author for automated posts
    default_author = get_default_author()

    # Create and save the blog post
    blog_post = BlogPost.objects.create(
        title=title,
        content=content,
        is_published=True,
        keywords="Punta Cana excursions, adventure tours, book now",
        meta_description=content[:160],
        featured_image=excursion.main_image,
        og_title=title,  # Updated to use the extracted H1 title
        og_description=f"Book your {title} adventure today!",
        author=default_author,
        rating=excursion.get_average_rating(),
        video_id=excursion.video_id,
    )

    # Save image URLs from excursion photos to the blog post
    for photo in excursion.photos.all():
        blog_post.images.create(image_url=photo.images.url)  # Ensure `BlogImage` has `image_url` field
    
    blog_post.save()
    return blog_post