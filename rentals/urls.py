from django.urls import path
from . import views

urlpatterns = [
    path('', views.rentals, name="rentals"),
    path('detail/<int:pk>', views.rental_details, name="rental_detail"),
    path('search/', views.input_search_result, name='rental_search_results'),
    path('newest/', views.newest_rentals, name='newest_rentals_result'),
    path('oldest/', views.oldest_rentals, name='oldest_rentals_result'),
    path('filter_by_ascend/', views.filter_by_price_ascend, name='filter_rentals_by_price_ascend'),
    path('filter_by_descend/', views.filter_by_price_descend, name='filter_rentals_by_price_descend'),
]