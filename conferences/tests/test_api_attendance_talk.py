from rest_framework.test import APITestCase
from conferences.models.attendance_talk import AttendanceTalk


class APIAttendanceTalkTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/attendancetalk')
        self.assertEqual(len(response.data['result']), 0)
