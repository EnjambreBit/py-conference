from rest_framework.test import APITestCase
from conferences.models.speakers_per_talk import SpeakerPerTalk


class APISpeakerPerTalkTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/speakerspertalk')
        self.assertEqual(len(response.data['result']), 0)
