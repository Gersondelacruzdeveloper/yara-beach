from django.urls import path
from . import views

urlpatterns = [
    # Path for excursion
    path('excursion_checkout', views.checkout, name="checkout"),
    path('checkout-success', views.checkout_success, name="checkout-success"),
    # Path for rental
    path('rental_checkout', views.checkout_rental, name="checkout_rental"),
    path('checkout-rental-success', views.checkout_rental_success,
         name="checkout-rental-success"),
]
