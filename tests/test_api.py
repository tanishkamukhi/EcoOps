import unittest
from unittest.mock import patch
from backend.vendor_api import plant_tree_api

class TestVendorAPI(unittest.TestCase):

    @patch("backend.vendor_api.requests.post")
    def test_successful_api_call(self, mock_post):
        mock_post.return_value.json.return_value = {"status": "success"}
        response = plant_tree_api("user123", 5)
        self.assertEqual(response["status"], "success")

    @patch("backend.vendor_api.requests.post")
    def test_failed_api_call(self, mock_post):
        mock_post.return_value.json.return_value = {"status": "error"}
        response = plant_tree_api("user123", 5)
        self.assertEqual(response["status"], "error")

if __name__ == "__main__":
    unittest.main()
