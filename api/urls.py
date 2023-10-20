from django.urls import path
from . import views

urlpatterns = [
    # excursions cart path
    path('', views.apiOverview),
    path('task-list/', views.task_list),
]
