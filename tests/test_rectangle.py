"""
Unit test for the Rectangle class.

"""
import unittest

from shape import Rectangle

class TestRectangle (unittest.TestCase):
    """Unit tests for the Rectangle class."""

    #__init__
    def test_init_blank_color(self):
        """Test that a blank color raises ValueError with correct message."""
        with self.assertRaises(ValueError) as context :
            Rectangle("  ", 5.0, 6.0)
        self.assertEqual(str(context.exception), "color cannot be blank")