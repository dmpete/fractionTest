import unittest
from fraction import Fraction


class TestMultiplication(unittest.TestCase):
    """Unit tests for the __mul__ method of the Fraction class."""

    # Basic multiplication tests
    def test_multiply_two_fractions(self):
        """Test multiplying two fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 8)

    def test_multiply_fractions_result_needs_normalization(self):
        """Test that multiplication result is normalized."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        # 2/3 * 3/4 = 6/12 = 1/2 (normalized)
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_multiply_fraction_by_integer(self):
        """Test multiplying a fraction by an integer."""
        f = Fraction(1, 4)
        result = f * 3
        # 1/4 * 3 = 3/4
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

    def test_multiply_integer_by_fraction(self):
        """Test multiplying an integer by a fraction (reverse order)."""
        f = Fraction(1, 4)
        result = 3 * f
        # 3 * 1/4 = 3/4
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

    # Identity and zero tests
    def test_multiply_by_one(self):
        """Test that multiplying by 1 returns an equivalent fraction."""
        f = Fraction(3, 5)
        result = f * 1
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 5)

    def test_multiply_by_zero(self):
        """Test that multiplying by 0 returns 0."""
        f = Fraction(3, 5)
        result = f * 0
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_zero_fraction_multiplication(self):
        """Test multiplying a zero fraction by another fraction."""
        f1 = Fraction(0, 1)
        f2 = Fraction(3, 5)
        result = f1 * f2
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    # Negative number tests
    def test_multiply_positive_and_negative_fractions(self):
        """Test multiplying a positive fraction by a negative fraction."""
        f1 = Fraction(2, 3)
        f2 = Fraction(-1, 4)
        result = f1 * f2
        # 2/3 * -1/4 = -2/12 = -1/6
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 6)

    def test_multiply_two_negative_fractions(self):
        """Test multiplying two negative fractions yields positive."""
        f1 = Fraction(-2, 3)
        f2 = Fraction(-1, 4)
        result = f1 * f2
        # -2/3 * -1/4 = 2/12 = 1/6
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_multiply_negative_integer_by_fraction(self):
        """Test multiplying a negative integer by a fraction."""
        f = Fraction(1, 4)
        result = f * (-2)
        # 1/4 * -2 = -2/4 = -1/2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 2)

    # Large number tests
    def test_multiply_large_fractions(self):
        """Test multiplying fractions with large numerators and denominators."""
        f1 = Fraction(100, 3)
        f2 = Fraction(7, 50)
        result = f1 * f2
        # 100/3 * 7/50 = 700/150 = 14/3
        self.assertEqual(result.numerator, 14)
        self.assertEqual(result.denominator, 3)

    # Fraction with denominator 1 tests
    def test_multiply_whole_number_fractions(self):
        """Test multiplying fractions that are whole numbers."""
        f1 = Fraction(2, 1)
        f2 = Fraction(3, 1)
        result = f1 * f2
        # 2 * 3 = 6
        self.assertEqual(result.numerator, 6)
        self.assertEqual(result.denominator, 1)

    # Commutative property test
    def test_multiplication_is_commutative(self):
        """Test that a * b = b * a."""
        f1 = Fraction(2, 5)
        f2 = Fraction(3, 7)
        result1 = f1 * f2
        result2 = f2 * f1
        self.assertEqual(result1.numerator, result2.numerator)
        self.assertEqual(result1.denominator, result2.denominator)

    # Associative property test
    def test_multiplication_is_associative(self):
        """Test that (a * b) * c = a * (b * c)."""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        f3 = Fraction(3, 4)
        result1 = (f1 * f2) * f3
        result2 = f1 * (f2 * f3)
        self.assertEqual(result1.numerator, result2.numerator)
        self.assertEqual(result1.denominator, result2.denominator)

    # Type error tests
    def test_multiply_by_unsupported_type_string(self):
        """Test that multiplying by a string raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            result = f * "hello"

    def test_multiply_by_unsupported_type_float(self):
        """Test that multiplying by a float raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            result = f * 1.5

    def test_multiply_by_unsupported_type_none(self):
        """Test that multiplying by None raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            result = f * None

    # Fraction with negative denominator (should be normalized)
    def test_multiply_resulting_in_normalized_negative(self):
        """Test that results with negative components are normalized correctly."""
        f1 = Fraction(1, -2)  # Should normalize to -1/2
        f2 = Fraction(2, 3)
        result = f1 * f2
        # -1/2 * 2/3 = -2/6 = -1/3
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

    # Multiplicative inverse property
    def test_multiply_fraction_by_reciprocal(self):
        """Test that f * (1/f) = 1."""
        f = Fraction(3, 5)
        reciprocal = Fraction(5, 3)
        result = f * reciprocal
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    # Result does not modify operands
    def test_multiplication_does_not_modify_operands(self):
        """Test that multiplication does not modify the original fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        original_f1_num = f1.numerator
        original_f1_den = f1.denominator
        original_f2_num = f2.numerator
        original_f2_den = f2.denominator
        result = f1 * f2
        self.assertEqual(f1.numerator, original_f1_num)
        self.assertEqual(f1.denominator, original_f1_den)
        self.assertEqual(f2.numerator, original_f2_num)
        self.assertEqual(f2.denominator, original_f2_den)


if __name__ == '__main__':
    unittest.main()
