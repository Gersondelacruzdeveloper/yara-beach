from django.urls import path
from . import views

urlpatterns = [
    path('', views.excursion, name="excursions"),
    path('detail/<int:pk>', views.excursion_details, name="excursion_detail"),
    path('add_images/<int:pk>', views.excursion_images, name="add_images"),
    path('form', views.add_excursions, name="form"),
    path('search/', views.input_search_result, name='search_results'),
    path('newest/', views.newest_excursions, name='newest_result'),
    path('oldest', views.oldest_excursions, name='oldest_result'),
    path('filter_by_ascend/', views.filter_by_price_ascend, name='filter_by_ascend'),
]