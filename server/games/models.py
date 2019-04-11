from django.db import models
from django.conf import settings


class Game(models.Model):
    name = models.CharField(max_length=64)
    description = models.Textfield(max_length=1024)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = settings.AUTH_USER_MODEL

    def __str__(self):
        return self.name
