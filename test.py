import unittest

from app import get_message

class TestApp(unittest.TestCase):
    def test_message(self):
        msg = get_message()
        self.assertEqual(msg, "Hello unit test!")

if __name__ == '__main__':
    unittest.main()
