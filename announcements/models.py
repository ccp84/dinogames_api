from django.db import models
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class Category(models.Model):
    """
    Model to hold categories for tagging announcements
    """
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    """
    Announcement model for news and event posts
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    lastupdated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-lastupdated"]
