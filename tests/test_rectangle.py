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

    def test_init_length_not_greater_than_zero(self):
        """Test that length <= 0 raises ValueError with correct message."""
        with self.assertRaises(ValueError) as context:
            Rectangle("red", 0, 6.0)
        self.assertEqual(str(context.exception),
                         "length must be a positive value") 

    def test_init_width_not_greater_than_zero(self):
            """Test that width <= 0 raises ValueError with correct message."""
            with self.assertRaises(ValueError) as context:
                Rectangle("red", 5.0, 0)
            self.assertEqual(str(context.exception),
                             "width must be a positive value") 

    def test_init_initializes_new_instance(self):
        """Test that a new instance stores the private attributes correctly."""
        rectangle = Rectangle("red", 5.0, 6.0)
        self.assertEqual(rectangle._color, "red")
        self.assertEqual(rectangle._length, 5.0)
        self.assertEqual(rectangle._width, 6.0)

    #Color property
    def test_color_returns_current_state(self):
        """Test that the color property returns the current state."""
        rectangle = Rectangle("blue", 5.0, 6.0)
        self.assertEqual(rectangle.color, "blue")

    #Area property
    def test_area_returns_rectangle_area(self):
       """Test that the area property returns the correct rectangle area."""
       rectangle = Rectangle("red", 5.0, 6.0)
       self.assertEqual(rectangle.area, 30.0)

    #Get_perimeter()
    def test_get_perimeter_returns_rectangle_perimeter(self):
        """Test that get_perimeter returns the correct rectangle perimeter."""
        rectangle = Rectangle("red", 5.0, 6.0)
        self.assertEqual(rectangle.get_perimeter(),22.0)

    #__str__()
    def test_str_returns_string_representation(self):
        """Test that __str__ returns the correct string representation."""
        rectangle = Rectangle("red", 5.0, 6.0)
        expected = ("The shape color is red. This rectangle has a length of "
                    "5.0cm and a width of 6.0cm.")
        self.assertEqual(str(rectangle), expected)

if __name__ == "__main__":
    unittest.main()