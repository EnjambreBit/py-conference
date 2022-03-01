from rest_framework.test import APITestCase
from conferences.models.social_media import SocialMedia


class APISocialMediaTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/socialmedia')
        self.assertEqual(len(response.data['result']), 0)
