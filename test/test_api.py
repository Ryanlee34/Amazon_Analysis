import os
import requests
from unittest.mock import patch
import unittest




class TestApi(unittest.TestCase):

    @patch("requests.get")
    def test_make_request(self, mock_get):
        mock_response = {
            "INR": 50,
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={os.getenv('API_KEY')}")


        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn("INR", response.json())







if __name__ == "__main__":
    unittest.main()