from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model


# Python builtin unittest
User = get_user_model


class UserTestCast(TestCase):
    def setUp(self):
        user_a = User(username='cigdem', email='cigdem@invalid.com')
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password('123_password')
        user_a.save()
        # print(user_a.id)
    # built in for asserting if the count of users equals to 1.

    def test_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
