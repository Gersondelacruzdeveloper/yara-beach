from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('comfirmation/', views.email_comfirmation_page, name="comfirmation"),
    # excursion bookings
    path('bookings/', views.customer_bookings, name="excursion-bookings"),
    # rental bookings
    path('bookings_rental/', views.customer_rental_bookings, name="rental-bookings"),
]
