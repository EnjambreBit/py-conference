from rest_framework.test import APITestCase
from conferences.models.grants import Grant


class APIGrantTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/grants")
        self.assertEqual(len(response.data["result"]), 0)
