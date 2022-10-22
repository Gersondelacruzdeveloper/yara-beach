from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


class TestAdminViews(TestCase):

    def setUp(self):
        """ Create test for login a for superuser"""
        username = "john"
        pswd = "johnpassword"
        email = 'lennon@thebeatles.com'
        self.client = Client()
        self.user = User.objects.create_superuser(username, email, pswd)
        self.client.login(username=username,email= email,password=pswd)
    
    def test_dashboard_view_page(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the dashboard page.
        """
        response = self.client.get("/administrator/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/administrator.html')

    def test_excursion_admin_view_page(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the excursion admin page.
        """
        response = self.client.get("/administrator/admin-excursion")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/excursions/admin_excursions.html')


    def test_rental_admin_view_page(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the rental admin page.
        """
        response = self.client.get("/administrator/admin-rental")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/rentals/admin_rentals.html')


    def test_add_rental_admin_view_page(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the add rental admin page.
        """
        response = self.client.get("/administrator/add_rental")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/rentals/add_rentals.html')


    def test_add_excursion_admin_view_page(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the add excursion admin page.
        """
        response = self.client.get("/administrator/add_excursion")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/excursions/add_excursions.html')

