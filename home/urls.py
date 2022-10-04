from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('comfirmation/', views.email_comfirmation_page, name="comfirmation"),
]
