from .models import Announcement, Category
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class Test_Create_Announcement(APITestCase):

    def setUp(self):
        test_category = Category.objects.create(title='news')
        test_user = CustomUser.objects.create_superuser(
            username='testuser', password='testpass1', firstname='test', lastname='name', email='mail@mail.co')
        test_announcement = Announcement.objects.create(
            category_id=1, title='title1', content='content1', author_id=1)

    def test_str_methods(self):
        announcement = Announcement.objects.get(id=1)
        category = Category.objects.get(id=1)
        self.assertEqual(str(announcement), "title1")
        self.assertEqual(str(category), "news")

    # def test_create_news(self):
    #     test_user2 = CustomUser.objects.create_superuser(
    #         username='testuser2', password='testpass2', firstname='test', lastname='name', email='mail@mail.co')
    #     self.client.login(username="testuser2", password="testpass2")
    #     response = self.client.post('/announcement/admin', {
    #         'category': 1, 'title': 'title2', 'content': 'content2'})
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_news(self):
        self.client.login(username="testuser", password="testpass1")
        response = self.client.get('/announcement/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
