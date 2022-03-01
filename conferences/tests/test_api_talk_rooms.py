from rest_framework.test import APITestCase
from conferences.models.talk_rooms import TalkRoom


class APITalkRoomTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/talkrooms")
        self.assertEqual(len(response.data["result"]), 0)
