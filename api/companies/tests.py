from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .models import Company, Team
from users.models import User



class CompanyTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_can_create_team(self):
        old_count = Team.objects.count()

        team_data = {"name": "Imaginary team"}
        self.response = self.client.post(
            reverse("teams", kwargs={"company_id": 0}),
            team_data,
            format="json"
        )

        self.assertEqual(self.response.status_code, 201)

        new_count = Team.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_delete_team(self):
        old_count = Team.objects.count()

        #creating user
        user_data = {"full_name": "Imaginary user", "email": "test_users@email.com",
                     "is_admin": True}
        self.response = self.client.post(
            reverse("admins"),
            user_data,
            format="json"
        )

        self.assertEqual(self.response.status_code, 201)

        # creating company
        company_data = {"full_name": "company", "mock_owner": 0}
        self.response = self.client.post(
            reverse("companies"),
            company_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, 201)

        # creating team
        team_data = {"name": "Imaginary team", "company": 0}
        self.response = self.client.post(
            reverse("teams"),
            team_data,
            format="json"
        )

        #deleting team
        before_delete_count = Team.objects.count()
        self.assertNotEqual(old_count, before_delete_count)

        self.response = self.client.delete(
            reverse("get_team"),
            team_data,
            format="json"
        )

        self.assertEqual(self.response.status_code, 200)
        after_delete_count = Team.objects.count()
        self.assertNotEqual(old_count, after_delete_count)


        def est_api_can_delete_company():
            # checking amount of company
            old_count = Company.objects.count()

            # creating mock_owner
            mock_owner = User(full_name = "mock_owner",is_admin= True)
            mock_owner.save()

            # creating editor
            mock_editor = User(full_name="mock_editor", is_admin=True)
            mock_editor.save()

            # creating company
            company_data= {"name": "Imaginary company",
                          "owner_id": "1",
                           "editor_id": "2"}
            self.response = self.client.post(
                reverse("companies"),
                team_data,
                format="json"
            )

            # checking new amount of company
            self.assertEqual(self.response.status_code, 200)
            new_count = Company.objects.count()
            self.assertNotEqual(old_count, new_count)

            self.response = self.client.delete (
                reverse("get_company", kwargs={"company_id": 1})
            )

            # get new amount of form
            after_delete_count = Company.objects.count()
            self.assertNotEqual(new_count, after_delete_count)

            self.assertEqual(self.response.status_code, 204)
