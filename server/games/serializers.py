from rest_framework import serializers

from games.models import Game


class GameSerialiazier(serializers.ModelSerializer):
    """Serializer for the games object"""

    class Meta:
        model = Game
        fields = ('name', 'description', 'created', 'last_updated',)
