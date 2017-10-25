from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .models import Company


class CompanyTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_can_create_team(self):
        old_count = Team.objects.count()

        team_data = {"name": "Imaginary team"}
        self.response = self.client.post(
            reverse(""), #????
            team_data,
            format="json"
        )

        self.assertEqual(self.response.status_code, 201)

        new_count = Team.objects.count()
        self.assertNotEqual(old_count, new_count)

    