from rest_framework.test import APITestCase
from conferences.models.talks import Talk


class APITalkTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/talks')
        self.assertEqual(len(response.data['result']), 0)
