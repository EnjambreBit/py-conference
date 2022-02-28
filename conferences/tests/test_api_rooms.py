from rest_framework.test import APITestCase
from conferences.models.rooms import Room


class APIRoomTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/rooms')
        self.assertEqual(len(response.data['result']), 0)
