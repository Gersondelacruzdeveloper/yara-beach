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

openai.api_key = settings.OPENAI_API_KEY

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

from datetime import datetime
import random
import string
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def generate_unique_title(excursion_title):
    # Generate a unique identifier with a random suffix and date
    unique_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    date_str = datetime.now().strftime('%Y-%m-%d')
    return f"{excursion_title} - {date_str} - {unique_suffix}"

def check_for_duplicate_title(excursion_title):
    # Check for existing posts with a similar title
    similar_titles = BlogPost.objects.filter(
        Q(title__icontains=excursion_title)
    )
    return similar_titles.exists()


def generate_blog_content(excursion_title, excursion_url, duration_time, price, transportation):
    # Create a content prompt for OpenAI with a detailed request for long content
    prompt = f"""
    Write a detailed blog post about {excursion_title} in HTML format. The blog post should be between 2,100 and 2,400 words. 
    Use appropriate HTML tags paragraphs, and lists. The content should include:
    1. An engaging introduction to capture the reader's interest.
    2. Detailed sections on the main attractions of the excursion.
    3. Reasons why someone should book this excursion.
    4. Personal stories or hypothetical examples to make the content more relatable.
    5. A strong call-to-action link at the end.
    6. Include keywords related to travel, adventure, and excursions to enhance SEO.
    """

    # Append duration if available
    if duration_time:
        prompt += f"Duration: {duration_time}. "

    # Append price if available
    if price:
        prompt += f"Price: {price}. "

    # Append transportation if available
    if transportation:
        prompt += f"Transportation: {transportation}. "

    # Add the additional information
    prompt += (
        "Highlight the main attractions, reasons to book, and add a call-to-action. "
        f"Include this link to the excursion: {excursion_url}."
    )

    # Make the API call to generate the blog content in multiple parts if needed
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional travel blogger."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3800,  # Maximize tokens for a longer output
        temperature=0.6
    )
    
    # Extract and return the generated content
    return response['choices'][0]['message']['content']


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
    print("creating posts")
    excursion = get_random_excursion()
    title = generate_unique_title(excursion.title)
    duration_time = excursion.duration_time
    price = excursion.price
    transportation = excursion.transportation
    
    # Check if a similar title already exists
    if check_for_duplicate_title(excursion.title):
        title = generate_unique_title(f"{excursion.title} - Unique")

    # Get excursion URL
    excursion_url = excursion.get_absolute_url()
    
    content = generate_blog_content(excursion.title, excursion_url, duration_time,price, transportation)
        
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
        og_title=excursion.title,
        og_description=f"Book your {excursion.title} adventure today!",
        author= default_author,
        rating = excursion.get_average_rating(), 
        video_id = excursion.video_id, 
    )
    # Save image URLs from excursion photos to the blog post
    for photo in excursion.photos.all():
        blog_post.images.create(image_url=photo.image_url)  # Ensure `BlogImage` has `image_url` field
    blog_post.save()
    return blog_post

