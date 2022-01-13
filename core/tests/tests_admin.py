from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # Runs before test suite to prepare to run the actual tests
    def setUp(self):
        # Create an admin user that can post GET and POST requests to the server
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@pmtague.com',
            password='password123'
        )

        # Use force login method on client to login admin user
        self.client.force_login(self.admin_user)
        # Create regular user
        self.user = get_user_model().objects.create_user(
            email='test@pmtague.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        # Use reverse method to fetch url, keeps from having to update it in all the tests
        url = reverse('admin:core_user_changelist')
        # Uses test client to perform http GET on the url above
        res = self.client.get(url)

        # Checks that GET returns 200 and res contains a name and email address
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
    
    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)