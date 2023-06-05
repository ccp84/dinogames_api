from django.db import models
from games.models import Game
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class Rating(models.Model):
    """
    Ratings model to hold thumbs up or down rating of games
    Rating field holds thumbs up - True, thumbs down - False or blank for not yet rated
    """
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game, related_name='ratings', on_delete=models.CASCADE
    )
    rating = models.BooleanField(blank=True)

    class Meta:
        """
        Each rating must be unique so that a user can only rate a game once
        """
        unique_together = ['author', 'game']

    def __str__(self):
        return f'{self.author} {self.game}'
