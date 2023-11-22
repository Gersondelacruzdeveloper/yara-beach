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
    path('seller', views.administrator_seller, name="seller"),
    path('paid_seller/<int:pk>', views.paid_seller, name="paid_seller"),
    path('seller_due_zero/<int:pk>', views.seller_due_zero, name="seller_due_zero"),
    path('pageVisit/', views.pageVisit, name="pageVisit"),
    path('create_auto_sellers/', views.create_auto_sellers, name="create_auto_sellers"),
    path('search_sellers/', views.search_sellers, name='search_sellers'),
    path('edit_seller/<int:pk>', views.edit_seller, name="edit_seller"),
    path('delete_seller/<int:pk>', views.delete_seller, name="delete_seller"),
    path('generate_users', views.generate_users, name="generate_users"),
    path('company_bookings', views.company_bookings, name="company_bookings"),
     # posts
    path('all_post', views.admin_post, name="all_post"),
    path('edit_post/<int:pk>', views.edit_post, name="edit_post"),
    path('delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('add_post', views.add_post, name="add_post"),

]
