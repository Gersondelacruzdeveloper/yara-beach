from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrator, name="administrator"),
    # admin Excursion url path
    path('admin-excursion', views.admin_excursions, name="admin-excursion"),
    path('add_excursion', views.add_excursions, name="add_excursion"),
    path('edit/<int:pk>', views.edit_excursions, name="edit_excursion"),
    path('delete_excursion/<int:pk>', views.delete_excursions, name="delete_excursion"),
    path('delete_excursions_photo/<int:pk>', views.delete_excursions_photos, name="delete_excursions_photo"),
    #admin Rentals url path
    path('admin-rental', views.admin_rentals, name="admin-rental"),
    path('add_rental', views.add_rentals, name="add_rental"),
    path('edit_rental/<int:pk>', views.edit_rentals, name="edit_rental"),
    path('delete_rentals_photo/<int:pk>', views.delete_rentals_photos, name="delete_rentals_photo"),
    path('delete_rental/<int:pk>', views.delete_rentals, name="delete_rental"),
]