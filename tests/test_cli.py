import unittest
from unittest.mock import MagicMock, patch

from lib.cli import CLI


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.api = MagicMock()
        self.config = MagicMock()
        self.cli = CLI(self.api, self.config)

    @patch("builtins.input", return_value="y")
    def test_handle_delete_with_confirmation_yes(self, mock_input):
        args = MagicMock()
        args.delete = "123"
        args.yes = False
        self.api.delete_paste.return_value = True

        self.cli.handle_delete(args)

        self.api.delete_paste.assert_called_once_with("123")

    @patch("builtins.input", return_value="n")
    def test_handle_delete_with_confirmation_no(self, mock_input):
        args = MagicMock()
        args.delete = "123"
        args.yes = False

        with self.assertRaises(SystemExit):
            self.cli.handle_delete(args)

        self.api.delete_paste.assert_not_called()

    def test_handle_delete_with_y_flag(self):
        args = MagicMock()
        args.delete = "123"
        args.yes = True
        self.api.delete_paste.return_value = True

        self.cli.handle_delete(args)

        self.api.delete_paste.assert_called_once_with("123")

    @patch("builtins.open")
    def test_handle_file_paste_success(self, mock_open):
        args = MagicMock()
        args.file = "test.txt"
        args.title = None
        args.folder = ""
        mock_open.return_value.__enter__.return_value.read.return_value = "test content"
        self.api.paste.return_value = "123"

        self.cli.handle_file_paste(args)

        self.api.paste.assert_called_once_with("test.txt", "test content", "")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_handle_file_paste_file_not_found(self, mock_open):
        args = MagicMock()
        args.file = "test.txt"

        with self.assertRaises(SystemExit):
            self.cli.handle_file_paste(args)

    def test_handle_contents_paste_success(self):
        args = MagicMock()
        args.contents = "test content"
        args.title = None
        args.folder = ""
        self.api.paste.return_value = "123"

        self.cli.handle_contents_paste(args)

        self.api.paste.assert_called_once_with(None, "test content", "")

    def test_handle_contents_paste_with_title_success(self):
        args = MagicMock()
        args.contents = "test content 2"
        args.title = "Test Title"
        args.folder = ""
        self.api.paste.return_value = "123"

        self.cli.handle_contents_paste(args)

        self.api.paste.assert_called_once_with("Test Title", "test content 2", "")

    def test_paste_and_print_empty_content(self):
        with self.assertRaises(SystemExit):
            self.cli.paste_and_print("title", " ", "")

    def test_paste_and_print_api_error(self):
        self.api.paste.return_value = False

        with self.assertRaises(SystemExit):
            self.cli.paste_and_print("title", "content", "")

    def test_handle_login_success(self):
        args = MagicMock()
        args.key = "test_key"
        args.base_url = "https://pastefy.ga"
        self.api.get_user.return_value = {"logged_in": True, "name": "test_user"}

        self.cli.handle_login(args)

        self.config.write_config.assert_called_once_with(
            {"key": "test_key", "baseUrl": "https://pastefy.ga"}
        )

    def test_handle_login_failure(self):
        args = MagicMock()
        args.key = "test_key"
        args.base_url = "https://pastefy.ga"
        self.api.get_user.return_value = {"logged_in": False}

        with self.assertRaises(SystemExit):
            self.cli.handle_login(args)


if __name__ == "__main__":
    unittest.main()
