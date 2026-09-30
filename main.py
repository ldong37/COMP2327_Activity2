"""A program to demonstrate the concepts from module 2."""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from shape import Triangle, Rectangle

def main():
    """The main entry point for the program.""" 

    # 1. Create an empty list that will later store Shape objects.
    shapes =[]

    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle_1 = Triangle ("red", 5.0, 6.0, 7.0)
        shapes.append(triangle_1)
    except ValueError as a:
        print(a)


    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle_1 = Rectangle ("red", 5.0, 6.0, 7.0)
        shapes.append(rectangle_1)
    except ValueError as b:
        print(b)


    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle_2 = Triangle("green", 3.0, 4.0, 5.0)
        shapes.append(triangle_2)
    except ValueError as e:
        print(e)

    try:
        rectangle_2 = Rectangle("yellow", 10.0, 2.5)
        shapes.append(rectangle_2)
    except ValueError as e:
        print(e)

    try:
        triangle_3 = Triangle("purple", 6.0, 8.0, 10.0)
        shapes.append(triangle_3)
    except ValueError as e:
        print(e)


    # 5. Iterate through the list of Shapes. On each iteration:
    #    - Print the shape.
    #    - Print the area of the shape to 2 decimal places.
    #    - Print the perimeter of the shape to 2 decimal places.
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area:.2f}")
        print(f"Perimeter: {shape.get_perimeter():.2f}")
        print()  

if __name__ == "__main__":
    main()
