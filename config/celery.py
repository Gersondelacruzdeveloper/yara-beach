from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from installed apps
app.autodiscover_tasks()

# Add Celery Beat schedule for periodic tasks
app.conf.beat_schedule = {
    'create-auto-blog-task': {
        'task': 'blog.tasks.create_auto_blog',  # Update 'your_blog_app' to your actual app name
        'schedule': crontab(hour=13, minute=13),  # Runs at 13:10 (1:10 PM)
    },
}

# Configuration to ensure broker retries on startup in Celery 6.0 and above
app.conf.broker_connection_retry_on_startup = True

# Optional: Test task (can be removed)
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
