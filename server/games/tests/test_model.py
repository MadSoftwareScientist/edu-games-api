from django.test import TestCase
from django.conf import settings

from rest_framework.test import APIClient

from models import Game


class ModelTests(TestCase):
    """Test the games API (public)"""

    fixtures = ['games_test_data', ]

    def setUp(self):
        self.client = APIClient()

    def test_game_str(self):
        """Test that game object is created correctly"""

        user = settings.AUTH_USER_MODEL.objects.get(email='test@test.fi')

        game = Game.objects.create(
            name='TestGame',
            description='Test game description.',
            owner=user,
        )

        self.assertEqual(str(game), game.name)
