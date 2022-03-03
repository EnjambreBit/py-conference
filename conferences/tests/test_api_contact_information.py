from rest_framework.test import APITestCase
from conferences.models.contact_information import ContactInformation


class APIContactInformationTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/contactinformation")
        self.assertEqual(len(response.data["result"]), 0)
