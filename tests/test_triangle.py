"""
Unit tests for Triangle class
"""
import unittest
from shape import Triangle


class TestTriangle (unittest.TestCase):

    """Unit tests for the Triangle class."""

#__init__ method
def test_init_blank_color(self):
    """ Test that a blank color raises ValueError with correct message """
    with self.assertRaises(ValueError) as context:
        Triangle(" ", 5.0, 6.0, 7.0)
    self.assertEqual(str(context.exception),"color cannot be blank")
