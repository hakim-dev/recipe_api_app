'''
sample test file
'''

from django.test import TestCase

from app import calc


class calcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add_numbers(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        res = calc.subtract_numbers(5, 11)
        self.assertEqual(res, 6)
