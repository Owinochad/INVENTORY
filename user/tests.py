from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LogoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_logout(self):
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, '/')
        # Ensure the user is logged out
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Logout')  # Assuming 'Logout' button is only visible to logged-in users