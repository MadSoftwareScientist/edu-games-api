from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient

LOGIN_USER_URL = reverse('rest_login')


class AuthenticationTests(TestCase):
    """Test authentication settings"""

    fixtures = ['testusers', ]

    def setUp(self):
        self.client = APIClient()

    def test_valid_login_success(self):
        """Login with correct credentials is successful"""

        res = self.client.login(username='test', password='test123')

        self.assertTrue(res)
