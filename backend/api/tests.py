from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class HealthCheckTests(APITestCase):
    def test_health_check_status(self):
        """
        Ensure the health check endpoint returns 200 OK.
        """
        url = reverse('health_check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')

class DataTests(APITestCase):
    def test_get_data_status(self):
        """
        Ensure the data endpoint returns 200 OK.
        """
        url = reverse('get_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'CI/CD Workshop')

class HomeTemplateTests(TestCase):
    def test_home_page_status(self):
        """
        Ensure the home page loads correctly.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CI/CD Workshop')
        self.assertContains(response, 'Django Templates')
