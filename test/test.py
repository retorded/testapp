import unittest

from core.app import *


class MyTestCase(unittest.TestCase):

    def test_sumtwointegers(self):
        self.assertEqual(sumtwointegers(1, 1), 2)

    def test_multiplytwointegers(self):
        self.assert_(multiplytwointegers(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
