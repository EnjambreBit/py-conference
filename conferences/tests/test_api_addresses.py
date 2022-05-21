from rest_framework.test import APITestCase
from conferences.models.addresses import Address


class APIAddressTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/addresses')
        self.assertEqual(len(response.data['result']), 0)
