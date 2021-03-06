from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        '''Test creating a new user with an email is successfull'''
        email = 'hamit@email.com'
        password = 'strong_password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_superuser(self):
        '''Test creating new superuser'''
        user = get_user_model().objects.create_superuser('email@mai.ru', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_email_normalized(self):
        '''Test the email for a new user in normalized'''
        email = 'user@DoMeN.CoM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123',
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Tests creating new user without email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'tets123')
