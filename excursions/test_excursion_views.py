from django.test import TestCase
from .models import Excursions

class TestExcursionViews(TestCase):

    def test_excursion_list_view(self):
        """
        Test excursion checkout llist view status response
        and template used.
        """
        response = self.client.get("/excursions/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excursions/excursions.html')


    def test_excursion_detail_view(self):
        """
        Test excursion checkout list view status response
        and template used.
        """
        excursion = Excursions.objects.create(
            title = 'sahona island',
            Price = 23.99,
            main_image = 'excursions/image/',
            image_name = 'sahona island image',
            description = 'descriotion of sahona',
            status = 'active',
        )
        excursion.save()
        excursion = Excursions.objects.get(id=excursion.id)
        response = self.client.get(f"/excursions/detail/{excursion.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excursions/excursion_details.html')

