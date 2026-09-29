from abc import ABC , abstractmethod

class Shape (ABC):
    """Represent a geometric shape with a color.
    Think of this class as a template for all shapes in the app. 
    It says what every shape needs to have, but you can't create a shape from it directly,you have to build specific shapes (like a triangle or rectangle) that fill in the actual area and perimeter formulas.
     
     """

