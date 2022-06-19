from rest_framework.test import APITestCase
from conferences.models.event_links import EventLink


class APIEventLinkTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/eventlinks')
        self.assertEqual(len(response.data['result']), 0)
