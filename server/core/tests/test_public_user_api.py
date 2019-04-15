from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


def get_user_detail_url(user_id):
    """Return url to retrieve user details"""
    return reverse('rest_user_details')


class PublicUserAPITests(TestCase):

    fixtures = ['testusers']

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_user_details(self):
        """Test that public api can retrieve public user profile"""

        res = self.client.get(get_user_detail_url(1))

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
