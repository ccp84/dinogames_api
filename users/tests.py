from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class Test_Create_Users(APITestCase):

    def test_create_superuser(self):
        test_user = CustomUser.objects.create_superuser(
            username='testuser', password='testpass1', firstname='test', lastname='name', email='mail@mail.co')
        self.assertIsInstance(test_user, CustomUser)
        self.assertEqual(str(test_user), "testuser")

    def test_error_no_username(self):
        self.assertRaises(ValueError, CustomUser.objects.create_user, username='',
                          password='testpass1', firstname='test', lastname='name', email='mail@mail.co')

    def test_error_no_email(self):
        self.assertRaises(ValueError, CustomUser.objects.create_user, username='testuser',
                          password='testpass1', firstname='test', lastname='name', email='')

    def test_error_superuser_not_staff(self):
        self.assertRaises(ValueError, CustomUser.objects.create_superuser, username='testuser',
                          password='testpass1', firstname='test', lastname='name', email='mail@mail.co', is_staff=False)

    def test_error_superuser_not_super(self):
        self.assertRaises(ValueError, CustomUser.objects.create_superuser, username='testuser',
                          password='testpass1', firstname='test', lastname='name', email='mail@mail.co', is_superuser=False)

    def test_create_user(self):
        response = self.client.post('/dj-rest-auth/registration/', {'username': 'newuser', 'password1': 'newpass1!',
                                                                    'password2': 'newpass1!', 'email': 'mail@mail.co', 'firstname': 'name', 'lastname': 'last'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_validate_user(self):
    #     self.assertRaises('ValidationError', CustomUser.objects.create_user, username='newuser', password1='newpass1!',
    #                       password2='newpass2!', email='mail@mail.co', firstname='name', lastname='last')
