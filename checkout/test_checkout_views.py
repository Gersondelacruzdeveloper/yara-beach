from django.test import TestCase
from .models import ExcursionOrder, AccommodationOrder
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


class TestCheckoutSuccessViews(TestCase):

    def setUp(self):
        """ Create test for login a for user"""
        username = "john"
        pswd = "johnpassword"
        email = 'lennon@thebeatles.com'
        self.client = Client()
        self.user = User.objects.create_user(username, email, pswd)
        self.client.login(username=username, email=email, password=pswd)

    def test_checkout_rental_success_view(self):
        """
        Test rental checkout success view status response
        and template used.
        """
        rental_order = AccommodationOrder.objects.create(
            rental_name='test name',
            order_number='015kjsdfjksdfjsbf5555dsf43545',
            full_name='test full name',
            image='uploaded/images',
            price=34.99,
            adult_qty=2,
            child_qty=1,
            check_in='2022-10-19',
            checkout='2022-10-20',
            customer_email='gerson@gmail.com',
            cellphone_number='07541148635',
            rental_type='Room',
            subtotal=70.04,
        )
        rental_order.save()

        rental_order_instance = AccommodationOrder.objects.get(
            id=rental_order.id)
        self.assertEqual(rental_order_instance.rental_name, 'test name')
        response = self.client.get("/checkout/checkout-rental-success")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/rental_success.html')

    def test_checkout_excursion_success_view(self):
        """
          Test excursion checkout success view status response
           and template used.
        """
        rental_order = ExcursionOrder.objects.create(
            excursion_name='test name',
            order_number='015kjsdfjksdfjsbf5555dsf43545',
            full_name='test full name',
            image='uploaded/images',
            price=34.99,
            adult_qty=2,
            child_qty=1,
            excursion_date='2022-10-19',
            customer_email='gerson@gmail.com',
            cellphone_number='07541148635',
            subtotal=70.04,
        )
        rental_order.save()

        rental_order_instance = ExcursionOrder.objects.get(id=rental_order.id)
        self.assertEqual(rental_order_instance.excursion_name, 'test name')
        response = self.client.get("/checkout/checkout-success")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/success.html')
