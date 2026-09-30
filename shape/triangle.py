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
        ValueError: The color is blank and the value of all sides are less or equal to zero and the sum of 2 sides must larger than the other side
        """

        super().__init__(color)

        if side_1 <= 0 :
            raise ValueError ("side_1 must be a positive value")

        if side_2 <= 0 :
            raise ValueError ("side_2 must be a positive value")

        if side_3 <= 0 :
            raise ValueError ("side_3 must be a positive value")

        if (side_1 + side_2 < side_3
            and side_2 + side_3 < side_1
            and side_3 + side_1 < side_2):
            raise ValueError ("The sides do not match with the Triangle Inequality Theorem ")
        
    
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

@property
def area(self) -> float:
    """
    Calculate and return the area of the area of the triangle by using Heron method:
    sp (half-perimeter of the triangle): (side_1 + side_2 + side_3)/2
    area = sqrt (sp*(sp-side_1)*(sp-side_2)*(sp-side_3))

    Returns:
       float:The value of triangle's area should be in square centimeter 
    """

    sp = (self._side_1 + self._side_2 + self._side_3) / 2
    return math.sqrt (sp * (sp-self._side_1) * (sp-self._side_2) * (sp-self._side_3))
    

def get_perimeter(self) ->float :
    """
    Calculate and return the perimeter of the triangle.
    Returns:
    float: The perimeter of the triangle in centimeters.
    """

    return self._side_1 + self._side_2 + self._side_3

def __str__(self) ->str:
    """
    Return a user-friendly string representation of the Triangle.
    
    Returns:
    str: A string describing the color and side lengths of the triangle.
    """

    return (f"{super().__str__()} This triangle has three sides with positive value"
            f"{self._side_1}, {self._side_2}, and {self._side_3} centimeters.")