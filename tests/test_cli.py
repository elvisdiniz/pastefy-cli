
import unittest
from unittest.mock import MagicMock, patch
from pastefy_cli import CLI

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

if __name__ == "__main__":
    unittest.main()
