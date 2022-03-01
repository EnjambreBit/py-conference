from rest_framework.test import APITestCase
from conferences.models.events import Event


class APIEventTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/events")
        self.assertEqual(len(response.data["result"]), 0)
