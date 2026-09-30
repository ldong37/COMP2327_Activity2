from shape.shape import Shape 

class Rectangle(Shape):
    """
    Represent a rectangle  geometric shape.

    A rectangle has 4 sides with 4 right angles.This class
    inherits from Shape and implements the abstract area and perimeter
    methods.
    """

def __init__(self,
             color: str,
             length:float,
             width: float):
    """
    Initialize a rectangle with a color, length, width
    Args:
    color (str): The color of the rectangle
    length (float): The length of opposing sides in centimeters.
    width (float): The width of the other sides in centimeters.

    Raises:
        ValueError: If the color is blank ,length and width of the rectangle is less or equal to zero.
    """

    super().__init__(color)

    if length <= 0:
        raise ValueError ("Length must be a positive value")

    if width <= 0:
        raise ValueError ("Width must be a positive value")

    self._length = length
    self._width = width

@property   
def area(self) -> float:
    """
    Calculate and return the area of the rectangle.
    Returns:
         float: The area of the rectangle is width * length
    """
    return self._length * self._width


def get_perimeter(self) -> float :
    """
    Calculate and return the perimeter of the rectangle.
    Returns:
         float: The perimeter of the rectangle is (width + length) *2
    """ 

    return (self._length + self._width) * 2

def __str__(self) -> str :
    """
    Return a user-friendly string representation of the Rectangle.

        Returns:
            str: A string describing the color, length, and width of the rectangle.
    """
    return (f"{super().__str__()} This rectangle has a length of "
                f"{self._length}cm and a width of {self._width}cm.")