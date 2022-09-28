from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrator, name="administrator"),
    path('admin-excursion', views.admin_excursions, name="admin-excursion"),
    path('admin-rental', views.admin_rentals, name="admin-rental"),
    path('add_excursion', views.add_excursions, name="add_excursion"),
    path('edit/<int:pk>', views.edit_excursions, name="edit_excursion"),
    path('delete_excursion/<int:pk>', views.delete_excursions, name="delete_excursion"),
]