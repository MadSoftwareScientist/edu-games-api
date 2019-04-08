from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

LOGIN_USER_URL = reverse('rest_login')
REGISTER_USER_URL = reverse('rest_register')


class AuthenticationTests(TestCase):
    """Test authentication settings"""

    fixtures = ['testusers', ]

    def setUp(self):
        self.client = APIClient()

    def test_valid_register_success(self):
        """Registration with correct data is succesful"""

        payload = {
            'username': 'test2',
            'email': 'test2@test.fi',
            'password1': 'Test!23Rest',
            'password2': 'Test!23Rest'

        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_valid_login_success(self):
        """Login with correct credentials is successful"""

        res = self.client.login(email='test@test.fi', password='test123')

        self.assertTrue(res)
