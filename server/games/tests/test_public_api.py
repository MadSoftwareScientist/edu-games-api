# from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from games.models import Game
from games.serializers import GameSerializer

GAMES_URL = reverse('games:game-list')


def get_game_detail_url(pk):
    """Return url for game's detail url"""
    return reverse('games:game-detail', args=[pk])


class PublicGamesAPITests(TestCase):
    """Test the publicly available games API"""

    fixtures = ['games_test_data', ]

    def setUp(self):
        self.client = APIClient()

    def test_retreive_games(self):
        """Test retrieving all the games"""

        res = self.client.get(GAMES_URL)

        games = Game.objects.all().order_by('-name')
        serializer = GameSerializer(games, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieving_one_game(self):
        """Test retrieving a specific game"""

        res = self.client.get(get_game_detail_url(1))

        game = Game.objects.get(pk=1)
        serializer = GameSerializer(game)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
