from rest_framework.test import APITestCase
from rest_framework import status
from ratings.models import Rating
from games.models import Game
from users.models import CustomUser


class Test_Create_Rating(APITestCase):

    def setUp(self):
        test_user1 = CustomUser.objects.create_user(
            username='testuser1', password='testpass1', firstname='test', lastname='name', email='mail@mail.co')
        test_user2 = CustomUser.objects.create_user(
            username='testuser2', password='testpass2', firstname='test', lastname='name', email='mail@mail.co')
        test_game = Game.objects.create(title='testgame')
        test_rating = Rating.objects.create(
            game_id=1, author_id=1, rating=True)

    def test_str_methods(self):
        rating = Rating.objects.get(id=1)
        self.assertEqual(
            str(rating), "testuser1 testgame")

    def test_validation_error(self):
        self.assertRaisesMessage(expected_exception='ValidationError',
                                 expected_message='You can only rate a game once', args=Rating.objects.create, game_id=1, author_id=1, rating=True)
