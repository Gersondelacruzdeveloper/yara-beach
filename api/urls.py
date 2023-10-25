from django.urls import path
from . import views

urlpatterns = [
    # excursions cart path
    path('', views.apiOverview),
    path('task-list/', views.task_list),
    path('add_task/',views.add_task ),
    path('api/task/<int:task_id>/', views.update_task),

]
