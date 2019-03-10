from unittest import TestCase, main

from exercises.multiples_3_5 import divisible_by, sum_of_values_divisible

class TestMultiples(TestCase):

    def test_divisible_by(self):

        divisors = [2, 5]
        value = 5

        self.assertIsNone(divisible_by(value=value, divisors=divisors))

    def test_not_divisible(self):
        divisors = [2, 3]
        value = 5

        with self.assertRaises(ValueError):
            divisible_by(value=value, divisors=divisors)

    def test_sum_of_divisors(self):
        divisors = [3, 5]
        max_value = 10

        sum_value = 23

        self.assertEqual(
            sum_value,
            sum_of_values_divisible(max_value, divisors)
            )
