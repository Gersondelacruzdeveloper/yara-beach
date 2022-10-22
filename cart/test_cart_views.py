from django.test import TestCase



class TestCartViews(TestCase):

    def test_excursion_cart_view_page(self):
        """
        Test for status code 200 response and correct
        template rendered when getting the cart page.
        """
        response = self.client.get("/cart/excursion-cart")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/excursions_cart.html')