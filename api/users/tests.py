from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .models import User
from .serializers import UserSerializer

class UserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_can_create_user(self):
        old_count = User.objects.count()

        user_data = {"full_name": "Imaginary user", "email": "test_users@email.com",
                     "is_admin": False}
        self.response = self.client.post(
            reverse("users"),
            user_data,
            format="json"
        )

        self.assertEqual(self.response.status_code, 201)

        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_delete_user(self):
        mock_user = User(full_name="mock user", email="testing.user@email.com", is_admin=False)
        mock_user.save()
        old_count = User.objects.count()
        self.response = self.client.delete(
            reverse("get_users", kwargs= {"user_id": mock_user.id})
        )

        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)

        self.assertEqual(self.response.status_code, 200)

    def test_api_can_retrieve_user(self):
        mock_user = User(full_name="mock user", email="testing.user@email.com", is_admin=False)
        mock_user.save()

        mock_user_second = User(full_name="mock user 2",
                                email="testing.user2@email.com", is_admin=False)
        mock_user_second.save()

        self.response = self.client.get(
            reverse("users")
        )

        all_users = User.objects.all()
        all_users_serialized = UserSerializer(all_users, many=True)
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(all_users_serialized.data, self.response)