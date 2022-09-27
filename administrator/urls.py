from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrator, name="administrator"),
    path('admin-excursion', views.admin_excursions, name="admin-excursion"),
]