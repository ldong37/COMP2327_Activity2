from abc import ABC , abstractmethod

class Shape (ABC):
    """
    Represent a geometric shape with a color.
    Think of this class as a template for all shapes in the app. 
    It says what every shape needs to have, but you can't create a shape from it directly,you have to build specific shapes (like a triangle or rectangle) that fill in the actual area and perimeter formulas.
    """

def __init__(self, color: str):
        """Initialize a Shape with the specified color.
        Args:
        color(str):The color of the shape
        Raises:
        Value Error: If the color arguement is a blank string
        """

        if color.strip() == "":
            raise ValueError("color cannot be blank")
            self._color = color.strip()

