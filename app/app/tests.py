from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test calculator functions."""

    def test_add_num(self):
        """Test adding two numbers."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_num(self):
        """Test subtracting two numbers."""
        res = calc.sub(5, 6)
        self.assertEqual(res, -1)
