from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from rest_auth.serializers import UserDetailsSerializer


def get_user_detail_url(user_id):
    return reverse('rest_user_details')


class PrivateUserAPITests(TestCase):
    """Test private auth API"""

    fixtures = ['testusers']

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_user_details(self):
        """Test that user can retrive their own information"""

        login = self.client.login(email='test@test.fi', password='test123')
        res = self.client.get(get_user_detail_url(4))

        user = get_user_model().objects.get(pk=4)
        serializer = UserDetailsSerializer(user)

        self.assertTrue(login)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.data['email'], 'test@test.fi')
