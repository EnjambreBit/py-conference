from rest_framework.test import APITestCase
from conferences.models.static_pages import StaticPage


class APIStaticPageTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/staticpages')
        self.assertEqual(len(response.data['result']), 0)
