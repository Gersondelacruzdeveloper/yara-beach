from django.urls import path
from . import views

urlpatterns = [
    path('', views.rentals, name="rentals"),
    path('detail/<int:pk>', views.rental_details, name="rental_detail"),
    path('search/', views.input_search_result, name='rental_search_results'),
    path('newest/', views.newest_rentals, name='newest_rentals_result'),
    path('oldest/', views.oldest_rentals, name='oldest_rentals_result'),
]