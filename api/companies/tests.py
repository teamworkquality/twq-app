from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .models import Company


class CompanyUserTest(TestCase):

    def setUp(self):
        self.client = APIClient()

