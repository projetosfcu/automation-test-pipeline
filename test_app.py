import unittest
from app import app

class SimpleFlaskTest(unittest.TestCase):

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()

    def test_homepage(self):
        """Test if homepage loads"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
