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
             length: float,
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