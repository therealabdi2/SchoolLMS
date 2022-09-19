from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import TeacherProfile


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.teacher = TeacherProfile.objects.create(
            name="Abc",
            email="abd@gmail.com",
            phone_number="+923345884763"
        )

    def test_model_content(self):
        self.assertEqual(self.teacher.name, "Abc")
        self.assertEqual(self.teacher.email, "abd@gmail.com")
        self.assertEqual(self.teacher.phone_number, "+923345884763")

    def test_api_listview(self):
        response = self.client.get(reverse("accounts:teacher_list_api"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TeacherProfile.objects.count(), 1)
        self.assertEqual(response.data[0]["name"], "Abc")
        self.assertEqual(response.data[0]["email"], "abd@gmail.com")
        self.assertEqual(response.data[0]["phone_number"], "+923345884763")

    def test_api_detailview(self):
        response = self.client.get(
            reverse("accounts:teacher_crud_api", args=[self.teacher.id]),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TeacherProfile.objects.count(), 1)
        self.assertContains(response, "Abc")

    # test update view
    def test_api_updateview(self):
        response = self.client.put(
            reverse("accounts:teacher_crud_api", args=[self.teacher.id]),
            {"name": "Ali", "email": "ali@gmail.com", "phone_number": "+923345884754"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TeacherProfile.objects.count(), 1)
        self.assertContains(response, "Ali")

    def test_api_deleteview(self):
        response = self.client.delete(
            reverse("accounts:teacher_crud_api", args=[self.teacher.id]),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TeacherProfile.objects.count(), 0)
        self.assertEqual(response.data, None)




