from rest_framework.test import APITestCase
from conferences.models.event_registrations import EventRegistration


class APIEventRegistrationTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/eventregistrations')
        self.assertEqual(len(response.data['result']), 0)
