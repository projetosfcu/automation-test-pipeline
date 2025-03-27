import unittest
from app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_status(self):
        """Test if the homepage returns a 200 status code"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        """Test if the homepage contains expected text"""
        response = self.app.get('/')
        self.assertIn(b'Hello, World!', response.data)  # Checking for a key phrase
        self.assertIn(b'Welcome to my Flask application!', response.data)

    def test_not_found_page(self):
        """Test if a non-existent page returns 404"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
