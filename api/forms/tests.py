from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .models import Form

class FormTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_can_delete_form(self):
        #criando mock object
        mock_form = Form(name="mock_name", has_time_limit = False)
        #insert in database
        mock_form.save()
        #getting amount of form before delete
        old_count = Form.objects.count()

        #deleting form
        self.response = self.client.delete(
            reverse("get_form", kwargs= {"form_id": mock_form.id, "company_id": 0})
        )

        #get new amount of form
        new_count = Form.objects.count()
        self.assertNotEqual(old_count, new_count)

        self.assertEqual(self.response.status_code, 204)