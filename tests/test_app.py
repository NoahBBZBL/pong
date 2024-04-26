# tests/test_app.py
import unittest
from unittest.mock import patch
from io import StringIO
from app import main

class TestApp(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue(), "Hello, John!\n")

if __name__ == '__main__':
    unittest.main()
