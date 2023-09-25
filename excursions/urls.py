from django.urls import path
from . import views

urlpatterns = [
    path('', views.excursion, name="excursions"),
    path('detail/<slug:slug>', views.excursion_details, name="excursion_detail"),
    path('add_images/<int:pk>', views.excursion_images, name="add_images"),
    path('search/', views.input_search_result, name='excursion_search_results'),
    path('newest/', views.newest_excursions, name='newest_result'),
    path('oldest', views.oldest_excursions, name='oldest_result'),
    path('filter_by_ascend/', views.filter_by_price_ascend, name='filter_by_ascend'),
    path('filter_by_descend/', views.filter_by_price_descend, name='filter_by_descend'),
    path('cart/', views.cart, name='cart'),
    path('reference/', views.create_reference, name='reference'),
    path('success/<str:reference_number>/', views.success_page, name='success_page'),
    path('cancel_excursion/<int:pk>', views.cancel_excursion, name="cancel_excursion"),

]