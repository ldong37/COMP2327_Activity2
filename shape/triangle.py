import math 
from shape.shape import Shape
class Triangle(Shape):
    """
    Represents a triangle geometric shape.
    A triangle is formed by connecting three sides not in a traight line .
    This class inherits from Shape and implements the abstract area and perimeter methods.
    """

    def __init__ (self,
                  color : str,
                  side_1 : float,
                  side_2 : float,
                  side_3 : float):

        """
        Initialize a triangle with a color and three side lengths.
        Args:
        color (str) :The color of the triangle
        side_1 (float) :The length of the first side of the triangle
        side_2 (float) :The length of the second side of the triangle
        side_3 (float) :The length of the third side of the triangle

        Raisess:
        ValueError: The color is blank and the value of all sides are less or equal to zero
        """