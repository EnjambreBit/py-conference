from rest_framework.test import APITestCase
from conferences.models.profiles import Profile


class APIProfileTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/profiles")
        self.assertEqual(len(response.data["result"]), 0)
