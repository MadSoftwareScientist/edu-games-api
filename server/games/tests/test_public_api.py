# from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Game

from ..serializers import GameSerializer

GAMES_URL = reverse('games:game-list')


class PublicGamesAPITests(TestCase):
    """Test the publicly available games API"""

    fixture = ['games_test_data', ]

    def setUp(self):
        self.client = APIClient()

    def test_retreive_games(self):
        """Test retrieving all the games"""

        res = self.client.get(GAMES_URL)

        games = Game.objects.all().order_by('-name')
        serializer = GameSerializer(games, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
