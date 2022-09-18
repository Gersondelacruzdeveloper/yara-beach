from django.urls import path
from . import views

urlpatterns = [
    path('', views.rentals, name="rentals"),
    path('detail/<int:pk>', views.rental_details, name="detail"),
]