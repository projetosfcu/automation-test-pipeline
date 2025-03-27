import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        """Test if the homepage returns correct response"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)
        self.assertIn(b'Welcome to my Flask application!', response.data)

if __name__ == "__main__":
    unittest.main()
