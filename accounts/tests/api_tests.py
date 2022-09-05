from django.test import TestCase
from django.urls import reverse

from accounts.models import TeacherProfile


# Create your tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        TeacherProfile.objects.create(
            name="Abdullah",
            email="abd@gmail.com",
            phone_number="1234"
        )

    def test_api_listview(self):
        response = self.client.get(reverse("accounts:teacher_view"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TeacherProfile.objects.count(), 1)

