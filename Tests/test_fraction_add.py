import unittest
from fraction import Fraction

class TestAddition(unittest.TestCase):

def test_add_two_fractions(self):
    "Test adding two fractions."
    f1 = Fraction(1,2)
    f2 = Fraction(1,3)
    result = f1 * f2
    self.assertEqual(result.numerator, 5)
    self.assertEquals(result.denominator, 6)


if __name__ == '__main__':
    unittest.main()

