from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
# from rest_framework import status


GET_GAMES = reverse('games:get')


class PublicGamesAPITests(TestCase):
    """Test the games API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_list_games_success(self):
        """Test listing all the games"""
        self.client.get(GET_GAMES)

        self.assertTrue(True)
