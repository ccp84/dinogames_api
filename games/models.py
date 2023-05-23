from django.db import models
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class Game(models.Model):
    """
    Model to contain all member games in the library
    """
    GAME_LENGTH_CHOICES = (
        (0, "<5"),
        (5, "5-10"),
        (10, "10-20"),
        (20, "20-40"),
        (40, "40-90"),
        (90, "90+")
    )
    title = models.CharField(max_length=100, unique=True)
    tags = models.TextField(blank=True)
    minplayers = models.IntegerField(default=1)
    maxplayers = models.IntegerField(default=4)
    playtime = models.IntegerField(
        choices=GAME_LENGTH_CHOICES, default=0)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return {self.title}
