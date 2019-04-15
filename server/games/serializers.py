from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    """Serializer for the games object"""

    class Meta:
        model = Game
        fields = ('id', 'name', 'description', 'created_at',
                  'updated_at', 'owner',)
        read_only_fields = ('id', 'owner', 'created_at', 'udated_at', )
