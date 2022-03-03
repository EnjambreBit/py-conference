from rest_framework.test import APITestCase
from conferences.models.sponsor_levels import SponsorLevel


class APISponsorLevelTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/sponsorlevels")
        self.assertEqual(len(response.data["result"]), 0)
