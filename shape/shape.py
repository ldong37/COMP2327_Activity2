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


@property

def color(self) -> str:
     """
     Get the color of the shape.
     Returns:
     str: The current color of the shape.
     """
     return self._color

@property
@abstractmethod
def area(self) ->float:
     """
     Calculate and return the area of the shape.
     Using this abstract method to implement by all subclasses to provide the specific area calculation

     Return:
     float : The area of the shape.
     """
     pass

@abstractmethod
def get_perimeter(self) -> float:
     """
     Calculate and return the perimeter of the shape
     Using this abstarct method to implement by all subclasses to provide the specific perimeter calculation

     Return:
     float : The perimeter calculation
     """
     pass

def __str__(self) -> str:
     """
     Return a user-friendly string representation of the shape.

     Returns:
      str: A string on the format 'The shape color is <color>.'
     """

     return f"The shape color is {self._color}."