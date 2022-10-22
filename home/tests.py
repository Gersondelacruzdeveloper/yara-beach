from django.test import TestCase

# Create your tests here.


def test_home_list_view(self):
    """
    Test home list view status response
    and template used.
    """
    response = self.client.get("/home/")
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/home.html')
