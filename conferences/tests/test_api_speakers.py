from rest_framework.test import APITestCase
from conferences.models.speakers import Speaker


class APISpeakerTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/speakers')
        self.assertEqual(len(response.data['result']), 0)
