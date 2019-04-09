from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

LOGIN_USER_URL = reverse('rest_login')
REGISTER_USER_URL = reverse('rest_register')
CHANGE_PASSWORD_URL = reverse('rest_password_change')


class AuthenticationTests(TestCase):
    """Test authentication settings"""

    fixtures = ['testusers', ]

    def setUp(self):
        self.client = APIClient()

    # TEST REGISTRATION API

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

        res = self.client.login(email='test2@test.fi', password='Test!23Rest')
        self.assertTrue(res)

    def test_registration_with_missing_email(self):
        """Test that registration fails if email is not provided"""

        payload = {
            'username': 'test2',
            'email': '',
            'password1': 'Test!23Rest',
            'password2': 'Test!23Rest'
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_missing_username(self):
        """Test that registration fails if username is not provided"""

        payload = {
            'username': '',
            'email': 'test2@test.fi',
            'password1': 'Test!23Rest',
            'password2': 'Test!23Rest'
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_missing_password(self):
        """Test that registration fails if passwords are not provided"""

        payload = {
            'username': 'test2',
            'email': 'test2@test.fi',
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_mismatching_passwords(self):
        """Test that registration fails if passwords do not match"""

        payload = {
            'username': 'test2',
            'email': 'test2@test.fi',
            'password1': 'Test!23Rest',
            'password2': 'Wrong!23Pass'
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_existing_email(self):
        """Test that registration fails if email is already used"""

        payload = {
            'username': 'test2',
            'email': 'test@test.fi',  # Exists in fixture
            'password1': 'Test!23Rest',
            'password2': 'Test!23Rest'
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_existing_username(self):
        """Test that registration fails if username is already used"""

        payload = {
            'username': 'test',  # Exists in fixture
            'email': 'test2@test.fi',
            'password1': 'Test!23Rest',
            'password2': 'Test!23Rest'
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # TEST LOGIN API

    def test_valid_login_success(self):
        """Login with correct credentials is successful"""

        res = self.client.login(email='test@test.fi', password='test123')

        self.assertTrue(res)

    def test_login_without_password(self):
        """Test that login fails if password is not provided"""

        res = self.client.login(email='test@test.fi', password='')

        self.assertFalse(res)

    def test_login_with_wrong_password(self):
        """Test that login fails with wrong password"""

        res = self.client.login(email='test@test.fi', password='wrongpass')

        self.assertFalse(res)

    def test_login_with_username(self):
        """Test that login fails if password is not provided"""

        res = self.client.login(email='test', password='test123')

        self.assertFalse(res)

    # TEST PASSWORD CHANGE API

    def test_succesful_password_change(self):
        """Test that user can change password"""

        email = 'test@test.fi'
        password = 'test123'
        payload = {
            'old_password': password,
            'new_password1': 'Test123Rest',
            'new_password2': 'Test123Rest',
        }
        res = self.client.login(email=email, password=password)
        self.assertTrue(res)

        res = self.client.post(CHANGE_PASSWORD_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_password_change_with_mismatching_passwords(self):
        """Test that user can change password"""

        email = 'test@test.fi'
        password = 'test123'
        payload = {
            'old_password': password,
            'new_password1': 'Test123Rest',
            'new_password2': 'wrongpass',
        }
        res = self.client.login(email=email, password=password)
        self.assertTrue(res)

        res = self.client.post(CHANGE_PASSWORD_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_changes_with_wrong_old_password(self):
        """Test that user can change password"""

        email = 'test@test.fi'
        payload = {
            'old_password': 'wrongpass',
            'new_password1': 'Test123Rest',
            'new_password2': 'Test123Rest',
        }
        res = self.client.login(email=email, password='test123')
        self.assertTrue(res)

        res = self.client.post(CHANGE_PASSWORD_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
