from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    # Test method names must all start with test_
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        # Test user info
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        # Create test user
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        # Assert that email and password created match those above
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        # Test user info
        email = 'test@LONDONAPPDEV.COM'
        # Create test user
        user = get_user_model().objects.create_user(email, 'test123')
        # Assert that the email address is stored in all lowercase
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londappdev.com',
            'test123'
        )
        # Superuser is provided as part of the permissions mixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
