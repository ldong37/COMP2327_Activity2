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
                  side_3 : float)