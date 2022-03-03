from rest_framework.test import APITestCase
from conferences.models.sponsors import Sponsor


class APISponsorTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/sponsors")
        self.assertEqual(len(response.data["result"]), 0)
