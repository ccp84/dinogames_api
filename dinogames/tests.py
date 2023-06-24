from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from games.models import Game
from users.models import CustomUser
from ratings.models import Rating


class Test_Permissions(APITestCase):

    def test_no_permission(self):
        test_game = Game.objects.create(title='title1')
        test_user1 = CustomUser.objects.create_user(
            username='testuser1', password='testpass1!', firstname='test', lastname='name', email='mail@mail.co')
        test_rating = Rating.objects.create(
            game_id=1, author_id=1, rating=True)
        response = self.client.get('/ratings/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
