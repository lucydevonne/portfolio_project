from django.test import TestCase, Client
from django.urls import reverse
import json

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_user(self):
        # Define test data
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        # Send a POST request to the /register/ endpoint
        response = self.client.post(reverse('register_user'), data=data)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected message
        self.assertEqual(response.json(), {'message': 'User registered successfully!'})
