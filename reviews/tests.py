from rest_framework.test import APITestCase
from rest_framework import status
from reviews.models import Review
from games.models import Game
from users.models import CustomUser


class Test_Create_Review(APITestCase):

    def setUp(self):
        test_user = CustomUser.objects.create_superuser(
            username='testuser', password='testpass1', firstname='test', lastname='name', email='mail@mail.co')
        test_game = Game.objects.create(title='testgame')
        test_review = Review.objects.create(
            game_id=1, content='content1', author_id=1)

    def test_str_methods(self):
        review = Review.objects.get(id=1)
        self.assertEqual(
            str(review), "Review of testgame by testuser")

    def test_get_reviews(self):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
