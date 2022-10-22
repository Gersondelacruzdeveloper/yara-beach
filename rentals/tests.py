from django.test import TestCase
from .models import Rentals

class TestRentalViews(TestCase):

    def test_rental_list_view(self):
        """
        Test excursion checkout llist view status response
        and template used.
        """
        response = self.client.get("/rentals/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/rentals.html')


    def test_rental_detail_view(self):
        """
        Test excursion checkout list view status response
        and template used.
        """
        rental = Rentals.objects.create(
            title = 'sahona island',
            Price = 23.99,
            main_image = 'excursions/image/',
            image_name = 'sahona island image',
            description = 'descriotion of sahona',
            ACCOM_type = 'Room',
            status = 'active',
        )
        rental.save()

        rental = Rentals.objects.get(id=rental.id)
        response = self.client.get(f"/rentals/detail/{rental.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rentals/rental_details.html')

