import unittest
from flask import json
from app import create_app
from app.config import TestConfig

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', data)

    def test_login(self):
        # First, register a user
        self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        # Then, login with the same user
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', data)

class ProfileTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Register and log in a user
        self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.access_token = json.loads(response.data)['access_token']

    def tearDown(self):
        self.app_context.pop()

    def test_get_profile(self):
        response = self.client.get('/main/profile', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('username', data)

    def test_update_profile(self):
        response = self.client.put('/main/profile', headers={
            'Authorization': f'Bearer {self.access_token}'
        }, json={
            'username': 'newusername'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
