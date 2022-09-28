import unittest

from src.calculator import calc


class MyTestCase(unittest.TestCase):

    def test_sumtwointegers(self):
        self.assertEquals(calc.sumtwointegers(1, 1), 2)

    def test_multiplytwointegers(self):
        self.assertEquals(calc.multiplytwointegers(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
