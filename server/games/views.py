from rest_framework import viewsets

from games.models import Game

from games.serializers import GameSerializer


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """A view set to get list of games and game details"""
    queryset = Game.objects.all().order_by('-name')
    serializer_class = GameSerializer
