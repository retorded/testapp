import unittest

from core.app import *


class MyTestCase(unittest.TestCase):

    def test_sumTwoInts(self):
        self.assertEqual(sumTwoInts(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
