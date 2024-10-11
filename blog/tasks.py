# blog/tasks.py
from celery import shared_task
from .views import create_blog_post  # Ensure the correct import

@shared_task
def create_auto_blog():
    create_blog_post()  # Calls the create_blog_post function from views.py
