from rest_framework.test import APITestCase
from conferences.models.countries import Country


class APICountryTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/countries")
        self.assertEqual(len(response.data["result"]), 0)
