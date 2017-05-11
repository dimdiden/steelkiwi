from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_index_view_with_logged_user(self):
        """
        If user is logged in, the page should contain url for
        displaying list of products for the last 24 hours
        """
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Get list of products for the last 24 hours")

    def test_index_view_with_not_logged_user(self):
        """
        If user is not logged in, the page should not contain url for
        displaying list of products for the last 24 hours
        """

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Get list of products for the last 24 hours")