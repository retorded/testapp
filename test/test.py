import unittest

from core.app import *


class MyTestCase(unittest.TestCase):

    def test_sumtwoints(self):
        self.assertEqual(sumtwoints(1, 1), 2)

    def test_multiplytwoints(self):
        self.assertEqual(multiplytwoints(1, 2), 2)


if __name__ == '__main__':
    unittest.main()
