from django.db import models
from games.models import Game
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class Review(models.Model):
    """
    Review model to hold data for library member reviews
    Authenticated members can create
    Resource owner can edit and delete
    """

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.TextField()
    lastupdated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-lastupdated"]

    def __str__(self):
        return f'Review of {self.game} by {self.author}'
