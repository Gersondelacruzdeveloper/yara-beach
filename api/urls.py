from django.urls import path
from . import views

urlpatterns = [
    # excursions cart path
    path('', views.apiOverview),
]
