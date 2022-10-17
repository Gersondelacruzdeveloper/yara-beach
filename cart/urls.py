from django.urls import path
from . import views

urlpatterns = [
    # excursions cart path
    path('excursion-cart', views.view_excursion_cart, name="excursion-cart"),
    path('add/<item_id>/',views.add_to_cart, name="add_to_cart"),
    path('update/<item_id>/',views.update_cart, name="cart_update"),
    path('remove/<item_id>/',views.remove_from_cart, name="remove_from_cart"),
    # rentals cart path
    path('rental-cart', views.view_rental_cart, name="rental-cart"),
    path('add_rental/<item_id>/',views.add_to_cart_rental, name="add_rental"),
]