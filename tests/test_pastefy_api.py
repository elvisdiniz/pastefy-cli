import unittest
from unittest.mock import MagicMock, patch

from lib.pastefy_api import PastefyAPI


class TestPastefyAPI(unittest.TestCase):
    def setUp(self):
        self.config = MagicMock()
        self.config.get.side_effect = lambda key: {
            "baseUrl": "https://pastefy.ga",
            "apiVersion": "v2",
            "key": "test_key",
        }.get(key)
        self.api = PastefyAPI(self.config)

    @patch("requests.post")
    def test_paste_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True, "paste": {"id": "123"}}
        mock_post.return_value = mock_response

        result = self.api.paste("title", "content")
        self.assertEqual(result, "123")

    @patch("requests.post")
    def test_paste_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": False}
        mock_post.return_value = mock_response

        result = self.api.paste("title", "content")
        self.assertFalse(result)

    @patch("requests.delete")
    def test_delete_paste_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}
        mock_delete.return_value = mock_response

        result = self.api.delete_paste("123")
        self.assertTrue(result)

    @patch("requests.delete")
    def test_delete_paste_failure(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": False}
        mock_delete.return_value = mock_response

        result = self.api.delete_paste("123")
        self.assertFalse(result)

    @patch("requests.get")
    def test_get_user(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"logged_in": True, "name": "test_user"}
        mock_get.return_value = mock_response

        result = self.api.get_user()
        self.assertEqual(result, {"logged_in": True, "name": "test_user"})


if __name__ == "__main__":
    unittest.main()
