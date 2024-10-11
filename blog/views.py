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

def generate_blog_content(excursion_title, excursion_url):
    # Create a content prompt for OpenAI
    prompt = (
        f"Write a detailed blog post about {excursion_title}. "
        f"Highlight the main attractions, reasons to book, and add a call-to-action. "
        f"Include this link to the excursion: {excursion_url}"
    )
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()

def get_random_excursion():
    # Filter only active excursions
    active_excursions = Excursions.objects.filter(status='Active')
    
    if not active_excursions.exists():
        raise ObjectDoesNotExist("No active excursions available.")
    
    # Choose a random active excursion
    random_excursion = random.choice(active_excursions)
    
    return random_excursion

def create_blog_post():
    print("creating posts")
    excursion = get_random_excursion()
    title = generate_unique_title(excursion.title)
    
    # Check if a similar title already exists
    if check_for_duplicate_title(excursion.title):
        title = generate_unique_title(f"{excursion.title} - Unique")

    # Get excursion URL
    excursion_url = excursion.get_absolute_url()
    
    content = generate_blog_content(excursion.title, excursion_url)
    
    # Create and save the blog post
    blog_post = BlogPost.objects.create(
        title=title,
        content=content,
        is_published=True,
        keywords="Punta Cana excursions, adventure tours, book now",
        meta_description=content[:160],
        featured_image=excursion.image,
        og_title=excursion.title,
        og_description=f"Book your {excursion.title} adventure today!"
    )
    blog_post.save()
    return blog_post

