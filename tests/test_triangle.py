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
            Triangle("  ", 5.0, 6.0, 7.0)
        self.assertEqual(str(context.exception),"color cannot be blank")

    def test_init_side_1_not_greater_than_zero(self):
        """Test that side_1 <= 0 raises ValueError with correct message"""
        with self.assertRaises(ValueError) as context:
            Triangle ("red",0,6.0,7.0)
        self.assertEqual(str(context.exception),"side_1 must be a positive value")

    def test_init_side_2_not_greater_than_zero(self):
        """Test that side_2 <= 0 raises ValueError with correct message"""
        with self.assertRaises(ValueError) as context:
            Triangle("red",5.0,0,7.0)
        self.assertEqual(str(context.exception),"side_2 must be a positive value")

    def test_init_side_3_not_greater_than_zero(self):
        """Test that side_3 <= 0 raises ValueError with correct message"""
        with self.assertRaises(ValueError) as context:
            Triangle("red",5.0,6.0,0)
        self.assertEqual(str(context.exception),"side_3 must be a positive value")

    def test_init_violates_triangle_inequality(self):
        """ Test that sides violating the Triangle Inequality raise ValueError"""
        with self.assertRaises(ValueError) as context:
            Triangle("red",1.0,2.0,10.0)
        self.assertEqual(str(context.exception),"The sides do not satisfy the Triangle Inequality Theorem")

    def test_init_initializes_new_instance(self):
        """Test that a new instance is properly initialized."""
        triangle = Triangle("red", 5.0, 6.0, 7.0)
        self.assertEqual(triangle.color, "red")
        self.assertEqual(triangle._side_1, 5.0)
        self.assertEqual(triangle._side_2, 6.0)
        self.assertEqual(triangle._side_3, 7.0)

    #Color property
    def test_color_returns_current_state(self):
       """Test that the color property returns the current state."""
       triangle = Triangle("blue", 5.0, 6.0, 7.0)
       self.assertEqual(triangle._color, "blue")


    #Area property
    def test_area_returns_triangle_area(self):
        """Test that the area property returns the correct triangle area."""
        triangle = Triangle("red", 3.0, 4.0, 5.0)
        self.assertEqual(triangle.area , 6.0)


    #get_perimeter()
    def test_get_perimeter_returns_triangle_perimeter(self):
       """ Test that get_perimeter returns the correct triangle perimeter . """
       triangle = Triangle("red", 5.0, 6.0, 7.0)
       self.assertEqual(triangle.get_perimeter(), 18.0)

    #__str__()
    def test_str_returns_string_representation(self):
        """Test that __str__ returns the correct string representation."""
        triangle = Triangle("red", 5.0, 6.0, 7.0)
        expected = ("The shape color is red. This triangle has three sides with lengths of "
                    "5.0, 6.0, and 7.0 centimeters.")
        self.assertEqual(str(triangle), expected)

if __name__ == "__main__":
    unittest.main()